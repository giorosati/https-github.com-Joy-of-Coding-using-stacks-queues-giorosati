# TEST FILE FOR COUNT LONGEST SUBSEQUENCE
# DO NOT MODIFY

from Queue import Queue
from count_longest import count_longest

def test_count_hello():
    assert count_longest(Queue([l for l in "hello"])) == 2

def test_count_m5():
    assert count_longest(Queue([l for l in "m" * 5])) == 5

def test_count_o3():
    assert count_longest(Queue([l for l in "hooop"])) == 3

def test_count_o4():
    assert count_longest(Queue([l for l in "oooohh"])) == 4

def test_count_oe4():
    assert count_longest(Queue([l for l in "oooohheeee"])) == 4

def test_count_e5():
    assert count_longest(Queue([l for l in "oooohheeeee"])) == 5

def test_count_e6():
    assert count_longest(Queue([l for l in "oooohhhhhaaeeeeee"])) == 6

def test_count_empty():
    assert count_longest(Queue([ ])) == 0

def test_count_m1():
    assert count_longest(Queue([l for l in "m"])) == 1

def test_count_sym():
    assert count_longest(Queue([l for l in "+__--___----__--_+"])) == 4
