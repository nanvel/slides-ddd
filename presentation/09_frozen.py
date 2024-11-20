from collections import namedtuple
from dataclasses import dataclass, replace

import attrs
from pydantic import BaseModel, ConfigDict

NamedTuplePosition = namedtuple('NamedTuplePosition', ['x', 'y', 'z'])


@attrs.define(frozen=True)
class AttrsPosition:
    x: int
    y: int
    z: int


@dataclass(frozen=True)
class DataClassPosition:
    x: int
    y: int
    z: int


class PydanticPosition(BaseModel):
    model_config = ConfigDict(frozen=True)

    x: int
    y: int
    z: int


def bad_function_primitives(x: int, y: int, z: int):
    # no problem here
    x = 2
    # ...
    return x, y, z


def bad_function(pos: AttrsPosition):
    # side effect
    pos.x = 2
    # ...
    return pos


if __name__ == '__main__':
    position = (1, 2, 3)
    print(position)

    position = NamedTuplePosition(1, 2, 3)
    print(position)
    print(position.x)

    position = AttrsPosition(0, 0, 0)
    # position.x = 2
    # attr.exceptions.FrozenInstanceError
    print(position)
    position = attrs.evolve(position, x=1)
    print(position)

    position = DataClassPosition(1, 2, 3)
    print(position)
    position = replace(position, x=0)
    print(position)

    position = PydanticPosition(x=1, y=2, z=3)
    print(position)
    print(position.model_dump())
    position = position.model_copy(update={'x': 0})
    print(position)
