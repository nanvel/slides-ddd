""" Entity object (aka reference object).

An object defined primarily by its identity.
Identities must be defined so that they can be effectively tracked.
"""
from dataclasses import dataclass


@dataclass
class Entity:
    id: int
    first_name: str
    last_name: str

    def __eq__(self, other):
        return self.id == other.id

    @property
    def uppercase_name(self):
        return ' '.join((self.first_name, self.last_name)).strip()
