from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    red: int
    green: int
    blue: int

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def to_css(self):
        return f'rgb({self.red}, {self.green}, {self.blue})'

    @classmethod
    def from_hsv(cls, h, s, v):
        h, s, v = h / 360, s / 100, v / 100
        i = int(h * 6)
        f = (h * 6) - i
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        r, g, b = [int(c * 255) for c in [(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)][i % 6]]
        return cls(r, g, b)


# ===
from typing import NewType

Quantity = NewType("Quantity", int)
Sku = NewType("Sku", str)


@dataclass(frozen=True)
class Order:
    order_id: int
    sku: Sku
    quantity: Quantity


# ===
class Age(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Age must be a positive integer")
        return super().__new__(cls, value)

    def is_adult(self):
        return self >= 18
