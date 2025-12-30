from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO, how are you") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("howdy") == 20
    assert value("Hey") == 20

def test_other():
    assert value("Good morning") == 100
    assert value("What's up") == 100
    assert value("Yo") == 100
    assert value("Bye") == 100
