from collatz import collatz

def test_collatz_63728127():
    assert collatz(63728127) == 949

def test_collatz_0():
    assert collatz(0) == 0

def test_collatz_0bad():
    assert collatz(0) != 1

def test_collatz_general():
    lengths = [0, 0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20,
               7, 7, 15, 15, 10, 23, 10, 111, 18, 18, 18, 106, 5, 26, 13, 13,
               21, 21, 21, 34, 8, 109, 8, 29, 16, 16, 16, 104, 11, 24, 24]
    for i, l in zip(range(len(lengths) + 1), lengths):
        assert collatz(i) == l
