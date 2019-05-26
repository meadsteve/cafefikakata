from collections import Counter
from typing import Dict

from cafe import money
from cafe.exceptions import NotEnoughStock, UnknownItem
from cafe.items import Item, Deal
from cafe.money import Krona
from cafe.orders import Order, Receipt


class Cafe:
    _prices: Dict[Item, Krona]
    _deals: Dict[Item, Deal]
    _stock: Dict[Item, int]

    def __init__(self, prices: Dict[Item, Krona], deals: Dict[Item, Deal]):
        self._prices = prices
        self._deals = deals
        self._stock = {item: 0 for item in self._prices.keys()}

    def ask_price(self, item: Item) -> Krona:
        try:
            return self._prices[item]
        except KeyError:
            raise UnknownItem(f"{item} is not on the menu")

    def place_order(self, order: Order) -> Receipt:
        grouped_items = Counter(order.items).items()
        prices = [self._order_item(item, quantity) for (item, quantity) in grouped_items]
        return Receipt(total=money.total(prices))

    def add_stock(self, item: Item, quantity: int) -> None:
        try:
            self._stock[item] += quantity
        except KeyError:
            raise UnknownItem(f"This shop can't stock {item}")

    @property
    def is_open(self):
        return any([item_stock > 0 for (_, item_stock) in self._stock.items()])

    def _enough_stock(self, item: Item, desired_quantity: int):
        try:
            return desired_quantity <= self._stock[item]
        except KeyError:
            raise UnknownItem(f"{item} is not on the menu")

    def _order_item(self, item: Item, quantity: int) -> Krona:
        if not self._enough_stock(item, quantity):
            raise NotEnoughStock(f"There's not enough {item} in stock")
        self._stock[item] -= quantity
        full_price = Deal(1, self.ask_price(item))
        deal = self._deals.get(item, full_price)
        return deal.price * (quantity // deal.quantity) \
            + full_price.price * (quantity % deal.quantity)
