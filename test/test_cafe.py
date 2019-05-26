from cafe.money import Krona
from cafe.cafe import Cafe


def test_money_can_be_equal():
    assert Krona(5) == Krona(5)


def test_cafe_have_prices():
    cafe = Cafe()
    assert cafe.get_prices("coffee") == Krona(5)
