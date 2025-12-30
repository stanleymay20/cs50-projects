from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_start_letters():
    assert is_valid("12CS") == False
    assert is_valid("A1") == False

def test_zero_rule():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS01") == False

def test_middle_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS-50") == False
