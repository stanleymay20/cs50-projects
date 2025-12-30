from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_out_of_range():
    assert validate("512.512.512.512") == False
    assert validate("256.100.100.100") == False
    assert validate("192.168.0.300") == False
