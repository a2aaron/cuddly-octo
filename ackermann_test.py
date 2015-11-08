from ackermann import ackermann

#format is m, n.

#n == 0
def test_ack_0_0():
    assert ackermann(0,0) == 1

def test_ack_1_0():
    assert ackermann(1,0) == 2

def test_ack_2_0():
    assert ackermann(2,0) == 3

def test_ack_3_0():
    assert ackermann(2,0) == 5

def test_ack_4_0():
    assert ackermann(2,0) == 13

#n == 1
def test_ack_0_1():
    assert ackermann(0,1) == 2

def test_ack_1_1():
    assert ackermann(1,1) == 3

def test_ack_2_1():
    assert ackermann(2,1) == 5

def test_ack_3_1():
    assert ackermann(3,1) == 13

#n == 2
def test_ack_0_2():
    assert ackermann(0,2) == 3

def test_ack_1_2():
    assert ackermann(1,2) == 4

def test_ack_2_2():
    assert ackermann(2,2) == 7

def test_ack_3_2():
    assert ackermann(3,2) == 29
