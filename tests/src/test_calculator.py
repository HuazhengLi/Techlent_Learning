from app.src.calculator import Calculator
cal = Calculator()

def test_add():
    assert cal.add(1,2) == 3
    assert cal.add(1,6) == 7

def test_subtract():
    assert cal.add(10,1) == 9
    assert cal.add(5,1) == 4
