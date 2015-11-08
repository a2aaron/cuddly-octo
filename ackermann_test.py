from ackermann import ackermann

def test_ack_m0():
    for n in range(100):
        assert ackermann(0, n) == n + 1

def test_ack_m1():
    for n in range(100):
        assert ackermann(1, n) == n + 2

def test_ack_m2():
    for n in range(100):
        assert ackermann(2, n) == 2*n + 3

def test_ack_m3():
    for n in range(7):
        assert ackermann(3, n) == 2**(n+3) - 3

def test_ack_4_0():
    assert ackermann(4, 0) == 2**2**2 - 3
