from dataclasses import dataclass
from typing import List, TypeVar, Generic

from cafe.items import Item
from cafe.money import Currency

LocalCurrency = TypeVar('LocalCurrency', bound=Currency)


@dataclass
class Order:
    items: List[Item]


@dataclass
class Receipt(Generic[LocalCurrency]):
    total: LocalCurrency