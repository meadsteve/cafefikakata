from dataclasses import dataclass
from typing import List

from cafe.items import Item
from cafe.money import Krona


@dataclass
class Order:
    items: List[Item]


@dataclass
class Receipt:
    total: Krona