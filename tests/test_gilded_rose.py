from gilded_rose import GildedRose
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
