import pytest

from cafe.money import Krona
from cafe.cafe import Item, Order, NotEnoughStock, UnknownItem, Cafe

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

expected_cafe_two_prices = [
    ("coffee", Krona(2)),
    ("fancy coffee", Krona(10)),
]


@pytest.mark.parametrize("item,expected_price", expected_cafe_one_prices)
def test_cafe_have_prices(item: Item, expected_price: Krona, cafe_one):
    assert cafe_one.ask_price(item) == expected_price


@pytest.mark.parametrize("item,expected_price", expected_cafe_two_prices)
def test_different_cafes_have_different_prices(item: Item, expected_price: Krona, cafe_two):
    assert cafe_two.ask_price(item) == expected_price


def test_a_cafe_can_give_you_a_receipt_for_the_order(cafe_one):
    order = Order(["coffee", "coffee", "kanelbulle"])
    receipt = cafe_one.place_order(order)
    assert receipt.total == Krona(20)


@pytest.mark.parametrize("order,expected_price", expected_cafe_one_deals)
def test_a_cafe_can_run_special_offers(order: Order, expected_price: Krona, cafe_one):
    assert cafe_one.place_order(order).total == expected_price


def test_cafe_two_can_run_different_deals(cafe_two):
    assert cafe_two.place_order(Order(["fancy coffee", "fancy coffee"])).total == Krona(15)


def test_cafes_throw_value_errors_if_they_dont_have_enough_stock(cafe_one):
    with pytest.raises(NotEnoughStock) as excinfo:
        cafe_one.place_order(Order(["fancy coffee"] * 20))
    assert "There's not enough fancy coffee in stock" in str(excinfo.value)


def test_placing_orders_lowers_stock(cafe_one):
    # The cafe starts with 10 coffees so this should be okay
    cafe_one.place_order(Order(["fancy coffee"] * 10))
    with pytest.raises(NotEnoughStock):
        cafe_one.place_order(Order(["fancy coffee"]))


def test_cafes_with_stock_are_open(cafe_one: Cafe):
    assert cafe_one.is_open


def test_cafes_without_stock_are_closed(cafe_without_stock: Cafe):
    assert not cafe_without_stock.is_open

def test_cafes_cant_be_stocked_with_things_not_on_the_menu(cafe_one: Cafe):
    with pytest.raises(UnknownItem):
        cafe_one.add_stock("bananas", 5)


def test_customers_cant_ask_the_price_of_items_not_on_the_menu(cafe_one: Cafe):
    with pytest.raises(UnknownItem):
        cafe_one.ask_price("flintstones chewable morphine")


def test_customers_cant_order_items_not_on_the_menu(cafe_one: Cafe):
    with pytest.raises(UnknownItem):
        cafe_one.place_order(Order(["coffee", "flintstones chewable morphine"]))


