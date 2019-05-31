from dataclasses import dataclass
from typing import TypeVar, Generic

from cafe.money import Currency

LocalCurrency = TypeVar('LocalCurrency', bound=Currency)


# Create a type for item. For now we'll use alias string for it
Item = str


@dataclass(frozen=True)
class Deal(Generic[LocalCurrency]):
    quantity: int
    price: LocalCurrency
