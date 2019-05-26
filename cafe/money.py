from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Krona:
    amount: int

    def __add__(self, other):
        if other == 0:
            return self
        if isinstance(other, Krona):
            return Krona(self.amount + other.amount)


def total(amounts: List[Krona]) -> Krona:
    return reduce(lambda t, x: t + x, amounts)
