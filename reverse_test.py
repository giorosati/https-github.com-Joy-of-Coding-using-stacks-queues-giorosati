# TEST FILE FOR REVERSE
# DO NOT MODIFY

from Queue import Queue
from reverse import reverse

def test_reverse_4():
    assert reverse(Queue(list(range(1, 5)))) == Queue([4, 3, 2, 1])

def test_reverse_0():
    assert reverse(Queue([])) == Queue([])

def test_reverse_1():
    assert reverse(Queue([0])) == Queue([0])

def test_reverse_str():
    assert reverse(Queue([l for l in "hello"])) == Queue([l for l in "olleh"])

def test_reverse_many():
    assert reverse(Queue(list(range(0,101,5)))) == Queue(list(range(100,-1,-5)))

def test_reverse_neg():
    assert reverse(Queue(list(range(1,-10, -1)))) == Queue(list(range(-9, 2)))

def test_reverse_nums():
    assert reverse(Queue([int(i) for i in "23762304"])) == Queue([int(i) for i in "40326732"])

def test_reverse_1s():
    assert reverse(Queue(["a"])) == Queue(["a"])

def test_reverse_1_neg():
    assert reverse(Queue([-5])) == Queue([-5])

def test_reverse_some():
    assert reverse(Queue(list(range(-5, 6)))) == Queue(list(range(5, -6, -1)))
