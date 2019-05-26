from dataclasses import dataclass

from cafe.money import Krona

# Create a type for item. For now we'll use alias string for it
Item = str


@dataclass
class Deal:
    quantity: int
    price: Krona
