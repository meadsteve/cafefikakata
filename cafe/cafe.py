from collections import Counter
from dataclasses import dataclass
from typing import Dict, List

from cafe import money
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


class NotEnoughStock(ValueError):
    pass


class UnknownItem(KeyError):
    pass


class Cafe:
    prices: Dict[Item, Krona]
    deals: Dict[Item, Deal]
    stock: Dict[Item, int]

    def __init__(self, prices: Dict[Item, Krona], deals: Dict[Item, Deal]):
        self.prices = prices
        self.deals = deals
        self.stock = {item: 0 for item in self.prices.keys()}

    def ask_price(self, item: Item) -> Krona:
        try:
            return self.prices[item]
        except KeyError:
            raise UnknownItem(f"{item} is not on the menu")

    def place_order(self, order: Order) -> Receipt:
        grouped_items = Counter(order.items).items()
        prices = [self._order_item(item, quantity) for (item, quantity) in grouped_items]
        return Receipt(total=money.total(prices))

    def add_stock(self, item: Item, quantity: int) -> None:
        try:
            self.stock[item] += quantity
        except KeyError:
            raise UnknownItem(f"This shop can't stock {item}")

    def _enough_stock(self, item: Item, desired_quantity: int):
        try:
            return desired_quantity <= self.stock[item]
        except KeyError:
            raise UnknownItem(f"{item} is not on the menu")

    def _order_item(self, item: Item, quantity: int) -> Krona:
        if not self._enough_stock(item, quantity):
            raise NotEnoughStock(f"There's not enough {item} in stock")
        self.stock[item] -= quantity
        full_price = Deal(1, self.ask_price(item))
        deal = self.deals.get(item, full_price)
        return deal.price * (quantity // deal.quantity) \
            + full_price.price * (quantity % deal.quantity)
