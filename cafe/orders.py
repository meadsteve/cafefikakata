from dataclasses import dataclass
from typing import List, TypeVar, Generic

from cafe.items import Item
from cafe.money import Currency

LocalCurrency = TypeVar('LocalCurrency', bound=Currency)


@dataclass(frozen=True)
class Order:
    items: List[Item]


@dataclass(frozen=True)
class Receipt(Generic[LocalCurrency]):
    total: LocalCurrency