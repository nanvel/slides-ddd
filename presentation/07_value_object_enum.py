""" Value object

Describe some characteristics of a thing.

Since value objects are immutable,
the value objects' behavior is free of side effects and is thread safe.
"""
from dataclasses import dataclass
from enum import Enum

MONDAY = "monday"  # a simple value object


@dataclass(frozen=True)
class Day:
    value: int
    name: str
    short_name: str


class DayOfWeek(int, Enum):
    MONDAY = Day(1, "Monday", "Mon")
    TUESDAY = Day(2, "Tuesday", "Tue")
    WEDNESDAY = Day(3, "Wednesday", "Wed")
    THURSDAY = Day(4, "Thursday", "Thu")
    FRIDAY = Day(5, "Friday", "Fri")
    SATURDAY = Day(6, "Saturday", "Sat")
    SUNDAY = Day(7, "Sunday", "Sun")

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._value_ = args[0].value
        return obj

    @property
    def is_weekend(self):
        return self in (self.SATURDAY, self.SUNDAY)

    @classmethod
    def get_weekends(cls):
        return cls.SATURDAY, cls.SUNDAY


if __name__ == '__main__':
    print(DayOfWeek.MONDAY.value)
    print(DayOfWeek.MONDAY.name)
    print(DayOfWeek(5).name)
    print(DayOfWeek(6).is_weekend)
    print(DayOfWeek.get_weekends())
    print(DayOfWeek.SATURDAY == DayOfWeek.SATURDAY)
    print(DayOfWeek.SATURDAY.value == 6)
