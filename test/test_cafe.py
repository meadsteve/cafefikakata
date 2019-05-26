import pytest

from cafe.money import Krona
from cafe.cafe import Cafe, Item


def test_money_can_be_equal():
    assert Krona(5) == Krona(5)


expected_prices = [
    ("coffee", Krona(5)),
    ("fancy coffee", Krona(8)),
    ("kanelbulle", Krona(10))
]


@pytest.mark.parametrize("item,expected_price", expected_prices)
def test_cafe_have_prices(item: Item, expected_price: Krona):
    cafe = Cafe()
    assert cafe.get_prices(item) == expected_price
