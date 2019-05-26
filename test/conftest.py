import pytest

from cafe.cafe import Cafe, Deal
from cafe.money import Krona


@pytest.fixture
def cafe_one() -> Cafe:
    return Cafe(
        {
            "coffee": Krona(5),
            "fancy coffee": Krona(8),
            "kanelbulle": Krona(10)
        },
        {
            "kanelbulle": Deal(3, Krona(25))
        }
    )


@pytest.fixture
def cafe_two() -> Cafe:
    return Cafe(
        {
            "coffee": Krona(2),
            "fancy coffee": Krona(10),
        },
        {
            "fancy coffee": Deal(2, Krona(15))
        }
    )