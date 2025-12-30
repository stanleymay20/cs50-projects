import pytest
from working import convert

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_evening_shift():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_night_shift():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_format_dash():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
