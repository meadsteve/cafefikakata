from typing import Dict, Optional

from cafe.money import Krona


# Create a type for item. For now we'll use alias string for it
Item = str


class Cafe:
    prices: Dict[Item, Krona] = {
        "coffee": Krona(5),
        "fancy coffee": Krona(8),
        "kanelbulle": Krona(10)
    }

    def get_prices(self, item: Item) -> Optional[Krona]:
        return self.prices.get(item)
