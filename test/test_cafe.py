import pytest

from cafe.money import Krona
from cafe.cafe import Cafe, Item, Order

expected_prices = [
    ("coffee", Krona(5)),
    ("fancy coffee", Krona(8)),
    ("kanelbulle", Krona(10))
]


@pytest.mark.parametrize("item,expected_price", expected_prices)
def test_cafe_have_prices(item: Item, expected_price: Krona):
    cafe = Cafe()
    assert cafe.get_price(item) == expected_price


def test_a_cafe_can_give_you_a_receipt_for_the_order():
    cafe = Cafe()
    order = Order(["coffee", "coffee", "kanelbulle"])
    receipt = cafe.get_receipt(order)
    assert receipt.total == Krona(20)
