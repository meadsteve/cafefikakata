import pytest

from cafe.money import Krona
from cafe.cafe import Cafe, Item, Order, Deal

expected_cafe_one_prices = [
    ("coffee", Krona(5)),
    ("fancy coffee", Krona(8)),
    ("kanelbulle", Krona(10))
]

expected_cafe_one_deals = [
    (Order(["kanelbulle", "kanelbulle", "kanelbulle"]), Krona(25)),
    (Order(["kanelbulle", "kanelbulle", "kanelbulle", "kanelbulle"]), Krona(35)),
    (Order(["kanelbulle", "kanelbulle", "kanelbulle", "coffee"]), Krona(30)),
]

cafe = Cafe(
    {
        "coffee": Krona(5),
        "fancy coffee": Krona(8),
        "kanelbulle": Krona(10)
    },
    {
        "kanelbulle": Deal(3, Krona(25))
    }
)

expected_cafe_two_prices = [
    ("coffee", Krona(2)),
    ("fancy coffee", Krona(10)),
]

cafe_two = Cafe(
    {
        "coffee": Krona(2),
        "fancy coffee": Krona(10),
    },
    {
        "fancy coffee": Deal(2, Krona(15))
    }
)


@pytest.mark.parametrize("item,expected_price", expected_cafe_one_prices)
def test_cafe_have_prices(item: Item, expected_price: Krona):
    assert cafe.get_price(item) == expected_price


@pytest.mark.parametrize("item,expected_price", expected_cafe_two_prices)
def test_different_cafes_have_different_prices(item: Item, expected_price: Krona):
    assert cafe_two.get_price(item) == expected_price


def test_a_cafe_can_give_you_a_receipt_for_the_order():
    order = Order(["coffee", "coffee", "kanelbulle"])
    receipt = cafe.get_receipt(order)
    assert receipt.total == Krona(20)


@pytest.mark.parametrize("order,expected_price", expected_cafe_one_deals)
def test_a_cafe_can_run_special_offers(order: Order, expected_price: Krona):
    assert cafe.get_receipt(order).total == expected_price


def test_cafe_two_can_run_different_deals():
    assert cafe_two.get_receipt(Order(["fancy coffee", "fancy coffee"])).total == Krona(15)
