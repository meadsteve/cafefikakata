from cafe.money import Krona


def test_money_can_be_equal():
    assert Krona(5) == Krona(5)
