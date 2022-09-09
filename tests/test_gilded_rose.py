from gilded_rose import GildedRose, Item
from tests.texttest_fixture import get_fixture_items, get_day_string


def test_gold():
    # Arrange
    with open("tests/gold.txt") as f:
        gold = f.read()

    gold_days = gold.rstrip().split("\n\n")

    items = get_fixture_items()

    # Act / Assert
    for day, gold_day in enumerate(gold_days):
        actual = get_day_string(day, items)
        assert actual == gold_day, f"Failed on day {day}"

        GildedRose(items).update_quality()


def test_conjured_items():
    # Arrange
    item = Item(name="Conjured Mana Cake", sell_in=3, quality=12)

    # Act / Assert
    GildedRose([item]).update_quality()
    assert item.sell_in == 2
    assert item.quality == 10, "Should degrade double 1, so 2"

    GildedRose([item]).update_quality()
    assert item.sell_in == 1
    assert item.quality == 8

    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 6

    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 2, "Should degrade double 2, so 4"

    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 0
