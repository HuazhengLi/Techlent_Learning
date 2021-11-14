from app.src.calculator import Calculator
cal = Calculator()

def test_add():
    assert cal.add(1,2) == 3
    assert cal.add(1,6) == 7

def test_subtract():
    assert cal.subtract(10,1) == 9
    assert cal.subtract(10,5) == 5
    assert cal.subtract(5,1) == 4
