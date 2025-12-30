import pytest
from datetime import date
from seasons import parse_date, calculate_minutes, minutes_to_words


def test_parse_date_valid():
    assert parse_date("2000-01-01") == date(2000, 1, 1)

def test_parse_date_invalid():
    with pytest.raises(SystemExit):
        parse_date("invalid-date")
    with pytest.raises(SystemExit):
        parse_date("2000/01/01")

def test_calculate_minutes():
    today = date.today()
    assert calculate_minutes(today) == 0

def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty five thousand six hundred minutes"
