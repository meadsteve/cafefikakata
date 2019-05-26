from dataclasses import dataclass
from typing import Dict, Optional, List

from cafe import money
from cafe.grouping import group_items
from cafe.money import Krona


# Create a type for item. For now we'll use alias string for it
Item = str


@dataclass
class Deal:
    quantity: int
    price: Krona


@dataclass
class Order:
    items: List[Item]


@dataclass
class Receipt:
    total: Krona


class Cafe:
    prices: Dict[Item, Krona]
    deals: Dict[Item, Deal]

    def __init__(self, prices: Dict[Item, Krona], deals: Dict[Item, Deal]):
        self.prices = prices
        self.deals = deals

    def get_price(self, item: Item) -> Krona:
        return self.prices[item]

    def get_receipt(self, order: Order) -> Receipt:
        grouped_items = group_items(order.items)
        prices = [self._get_total(item, quantity) for (item, quantity) in grouped_items]
        return Receipt(total=money.total(prices))

    def _get_total(self, item: Item, quantity: int) -> Krona:
        full_price = Deal(1, self.get_price(item))
        deal = self.deals.get(item, full_price)
        return deal.price * (quantity // deal.quantity) \
            + full_price.price * (quantity % deal.quantity)
