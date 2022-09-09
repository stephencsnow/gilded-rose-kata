class ItemWrapper:
    def __init__(self, item: "Item"):
        self.item = item

    def update(self):
        self._update_quality(self.item.sell_in)
        self._update_sell_in()

    def _update_quality(self, sell_in: int):
        if (
            self.item.name != "Aged Brie"
            and self.item.name != "Backstage passes to a TAFKAL80ETC concert"
        ):
            if self.item.quality > 0:
                if self.item.name != "Sulfuras, Hand of Ragnaros":
                    self.item.quality = self.item.quality - 1
        else:
            if self.item.quality < 50:
                self.item.quality = self.item.quality + 1
                if self.item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if sell_in < 11:
                        if self.item.quality < 50:
                            self.item.quality = self.item.quality + 1
                    if sell_in < 6:
                        if self.item.quality < 50:
                            self.item.quality = self.item.quality + 1
        if sell_in <= 0:
            if self.item.name != "Aged Brie":
                if self.item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.item.quality > 0:
                        if self.item.name != "Sulfuras, Hand of Ragnaros":
                            self.item.quality = self.item.quality - 1
                else:
                    self.item.quality = self.item.quality - self.item.quality
            else:
                if self.item.quality < 50:
                    self.item.quality = self.item.quality + 1

    def _update_sell_in(self):
        if self.item.name != "Sulfuras, Hand of Ragnaros":
            self.item.sell_in = self.item.sell_in - 1


class GildedRose(object):
    def __init__(self, items):
        self.items = [ItemWrapper(item) for item in items]

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
