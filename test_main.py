import main

def test_addTwoNumbers():
    assert main.addTwoNumbers(1, 2) == 3
    assert main.addTwoNumbers(0, 5) == 5
    assert main.addTwoNumbers(-1, 7) == 6

if __name__ == "__main__":
    test_addTwoNumbers()