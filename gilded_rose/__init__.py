class ItemWrapper:
    def __init__(self, item: "Item"):
        self.item = item

    def update(self):
        self._update_quality(self.item.sell_in)
        self._update_sell_in()

    def _increment_quality(self, amount: int = 1):
        """Increment quality, but do not go above the max"""
        MAX_QUALITY = 50
        self.item.quality = min([MAX_QUALITY, self.item.quality + amount])

    def _decrement_quality(self, amount: int = 1):
        """Decrement quality, but do not go below 0"""
        self.item.quality = max([0, self.item.quality - amount])

    def _update_quality(self, sell_in: int):
        if sell_in <= 0:
            self._decrement_quality(2)
        else:
            self._decrement_quality(1)

    def _update_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1


class AgedBrie(ItemWrapper):
    def _update_quality(self, sell_in: int):
        if sell_in <= 0:
            self._increment_quality(2)
        else:
            self._increment_quality(1)


class Sulfuras(ItemWrapper):
    def _update_quality(self, sell_in: int):
        pass

    def _update_sell_in(self):
        pass


class BackstagePasses(ItemWrapper):
    def _update_quality(self, sell_in: int):
        if sell_in <= 0:
            self.item.quality = 0
        elif sell_in <= 5:
            self._increment_quality(3)
        elif sell_in <= 10:
            self._increment_quality(2)
        else:
            self._increment_quality(1)


class GenericItem(ItemWrapper):
    pass


class GildedRose(object):
    def __init__(self, items):
        self.items: list[ItemWrapper] = []
        for item in items:
            tokenized_name = [name.rstrip(",") for name in item.name.split()]
            match tokenized_name:
                case ["Aged", "Brie"]:
                    self.items.append(AgedBrie(item))
                case ["Sulfuras", *rest]:
                    self.items.append(Sulfuras(item))
                case ["Backstage", "passes", *rest]:
                    self.items.append(BackstagePasses(item))
                case _:
                    self.items.append(GenericItem(item))

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
