from cafe import money
from cafe.money import Krona


def test_money_can_be_equal():
    assert Krona(5) == Krona(5)


def test_money_can_be_totalled():
    assert money.total([Krona(5), Krona(2), Krona(1)]) == Krona(8)


def test_money_can_be_multiplied():
    assert Krona(5) * 2 == Krona(10)
