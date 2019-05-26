from dataclasses import dataclass
from typing import Dict, Optional, List

from cafe import money
from cafe.money import Krona


# Create a type for item. For now we'll use alias string for it
Item = str


@dataclass
class Order:
    items: List[Item]


@dataclass
class Receipt:
    total: Krona


class Cafe:
    prices: Dict[Item, Krona] = {
        "coffee": Krona(5),
        "fancy coffee": Krona(8),
        "kanelbulle": Krona(10)
    }

    def get_price(self, item: Item) -> Krona:
        return self.prices[item]

    def get_receipt(self, order: Order) -> Receipt:
        prices = [self.get_price(item) for item in order.items]
        return Receipt(total=money.total(prices))
