from cafe import money
from cafe.grouping import group_items
from cafe.money import Krona


def test_items_that_are_the_same_are_grouped():
    assert group_items(["coffee", "coffee"]) == [("coffee", 2)]


def test_items_that_arent_the_same_get_their_own_group():
    assert group_items(["coffee", "fancy coffee", "coffee"]) == [("coffee", 2), ("fancy coffee", 1)]
