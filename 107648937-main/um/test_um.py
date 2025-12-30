from um import count

def test_one_um():
    assert count("um") == 1

def test_one_um_punctuation():
    assert count("um?") == 1

def test_um_in_sentence():
    assert count("Um, thanks for the album.") == 1

def test_two_ums():
    assert count("Um, thanks, um...") == 2

def test_um_as_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("platinum") == 0

def test_multiple_lines():
    assert count("um um um") == 3
    assert count("Um. Um! Um?") == 3
