from collections import Counter
from typing import List, Tuple, TypeVar

T = TypeVar("T")


def group_items(items: List[T]) -> List[Tuple[T, int]]:
    return [item for item in Counter(items).items()]
