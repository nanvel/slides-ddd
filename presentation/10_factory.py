""" Factory - a mechanism for encapsulating complex creation logic
and abstracting the type of created object for the sake of a client

When creation of an object, or an entire aggregate,
becomes complicated or reveals too much of the internal structure,
factories provide encapsulation.

In domain-driven design, an object's creation is often separated
from the object itself.
"""
from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class Color:
    red: int
    green: int
    blue: int


class ColorFactory:
    def from_hsl(self, h: float, s: float, l: float):
        h, s, l = h / 360, s / 100, l / 100
        if s == 0:
            r = g = b = int(l * 255)
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = self._hue_to_rgb(p, q, h + 1 / 3)
            g = self._hue_to_rgb(p, q, h)
            b = self._hue_to_rgb(p, q, h - 1 / 3)
        return Color(r, g, b)

    def from_df(self, df: pd.DataFrame):
        """Find average color from a DataFrame"""
        r, g, b = df.mean().round().astype(int)
        return Color(r, g, b)

    def _hue_to_rgb(self, p, q, t):
        if t < 0:
            t += 1
        if t > 1:
            t -= 1
        if t < 1 / 6:
            return p + (q - p) * 6 * t
        if t < 1 / 2:
            return q
        if t < 2 / 3:
            return p + (q - p) * (2 / 3 - t) * 6
        return p
