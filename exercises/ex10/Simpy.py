"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730574005"


class Simpy:
    """Class Simpy."""
    values: list[float]

    def __init__(self, list: list[float]):
        """Initializes Simpy."""
        self.values = list

    def __repr__(self) -> str:
        """Produces a string representation."""
        return f"Simpy({self.values})"

    def fill(self, float: float, values: int) -> None:
        """Fill a Simpy's value with a specific number of repeating values."""
        i: int = 0
        self.values = []
        while i < values:
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in values attribute with range of values."""
        assert step != 0.0, "Cannot have 0.0 as a step value."
        i: int = start
        self.values = [start]
        while i != stop:
            i += step
            self.values.append(i)
        self.values.pop()

    def sum(self) -> float:
        """Compute and return the sum of all items in values."""
        self = sum(self.values)
        return self
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds together overload."""
        result: Simpy = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i + rhs)
        else:
            assert len(self.values) == len(rhs.values), "Must be same length"
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1
        return Simpy(result)
        
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Powers overload."""
        result: Simpy = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i ** rhs)
        else:
            assert len(self.values) == len(rhs.values), "Must be same length"
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] ** rhs.values[i])
                i += 1
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks to see if 2 Simpys are equal."""
        result: Simpy = []
        if isinstance(rhs, float):
            for i in self.values:
                if i == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks to see if one Simpy is greater than the other."""
        result: Simpy = []
        if isinstance(rhs, float):
            for i in self.values:
                if i > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows for subscription notation overload."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = []
            for item in range(0, len(self.values)):
                if rhs[item] is True:
                    result.append(self.values[item])
            return Simpy(result)