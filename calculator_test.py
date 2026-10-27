from calculator import Calculator


def test_adds_two_numbers():
    assert Calculator().add(2, 3) == 5
    