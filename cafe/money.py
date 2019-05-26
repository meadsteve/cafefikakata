from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Currency:
    amount: int

    def __add__(self, other):
        if other == 0:
            return self
        if type(other) == type(self):
            return self.__class__(self.amount + other.amount)

    def __mul__(self, other):
        return self.__class__(self.amount * other)


class Krona(Currency):
    pass


def total(amounts: List[Krona]) -> Krona:
    return reduce(lambda t, x: t + x, amounts)
