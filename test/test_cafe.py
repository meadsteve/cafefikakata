import pytest

from cafe.money import Krona
from cafe.cafe import Cafe, Item, Order

cafe = Cafe()

expected_prices = [
    ("coffee", Krona(5)),
    ("fancy coffee", Krona(8)),
    ("kanelbulle", Krona(10))
]


@pytest.mark.parametrize("item,expected_price", expected_prices)
def test_cafe_have_prices(item: Item, expected_price: Krona):
    assert cafe.get_price(item) == expected_price


def test_a_cafe_can_give_you_a_receipt_for_the_order():
    order = Order(["coffee", "coffee", "kanelbulle"])
    receipt = cafe.get_receipt(order)
    assert receipt.total == Krona(20)


expected_deals = [
    (Order(["kanelbulle", "kanelbulle", "kanelbulle"]), Krona(25)),
    (Order(["kanelbulle", "kanelbulle", "kanelbulle", "kanelbulle"]), Krona(35)),
    (Order(["kanelbulle", "kanelbulle", "kanelbulle", "coffee"]), Krona(30)),
]


@pytest.mark.parametrize("order,expected_price", expected_deals)
def test_a_cafe_can_run_special_offers(order: Order, expected_price: Krona):
    assert cafe.get_receipt(order).total == expected_price
