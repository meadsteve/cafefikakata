import pytest

from cafe.cafe import Cafe, Deal
from cafe.money import Krona


@pytest.fixture
def cafe_one() -> Cafe:
    cafe = Cafe({"coffee": Krona(5), "fancy coffee": Krona(8), "kanelbulle": Krona(10)},
                {"kanelbulle": Deal(3, Krona(25))})
    cafe.add_stock("coffee", 10)
    cafe.add_stock("fancy coffee", 10)
    cafe.add_stock("kanelbulle", 10)
    return cafe


@pytest.fixture
def cafe_two() -> Cafe:
    cafe = Cafe({"coffee": Krona(2), "fancy coffee": Krona(10), }, {"fancy coffee": Deal(2, Krona(15))})
    cafe.add_stock("coffee", 10)
    cafe.add_stock("fancy coffee", 10)
    return cafe


@pytest.fixture
def cafe_without_stock() -> Cafe:
    return Cafe({"coffee": Krona(2), "fancy coffee": Krona(10), }, {"fancy coffee": Deal(2, Krona(15))})

