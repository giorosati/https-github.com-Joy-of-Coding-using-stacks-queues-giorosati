# TEST FILE FOR GENERATE BINARY NUMBERS
# DO NOT MODIFY

from Queue import Queue
from generate_binary import generate_binary_numbers

def test_binary_0():
    assert generate_binary_numbers(0)  == Queue([])

def test_binary_1():
    assert generate_binary_numbers(1)  == Queue(['1'])

def test_binary_2():
    assert generate_binary_numbers(2)  == Queue(['1', '10'])

def test_binary_3():
    assert generate_binary_numbers(3)  == Queue(['1', '10', '11'])

def test_binary_4():
    assert generate_binary_numbers(4)  == Queue(['1', '10', '11', '100'])

def test_binary_5():
    assert generate_binary_numbers(5)  == Queue(['1', '10', '11', '100', '101'])

def test_binary_6():
    assert generate_binary_numbers(6)  == Queue(['1', '10', '11', '100', '101', '110'])

def test_binary_7():
    assert generate_binary_numbers(7)  == Queue(['1', '10', '11', '100', '101', '110', '111'])

def test_binary_8():
    assert generate_binary_numbers(8)  == Queue(['1', '10', '11', '100', '101', '110', '111', '1000'])

def test_binary_neg():
    assert generate_binary_numbers(-1) == Queue([])

def test_binary_12():
    assert generate_binary_numbers(12) == Queue(['1', '10', '11', '100', '101', '110', '111', \
                                                 '1000', '1001', '1010', '1011', '1100'])

def test_binary_15():
    assert generate_binary_numbers(15) == Queue(['1', '10', '11', '100', '101', '110', '111', \
                                                 '1000', '1001', '1010', '1011', '1100', '1101', \
                                                 '1110', '1111'])

def test_binary_31():
    assert generate_binary_numbers(31) == Queue(['1', '10', '11', '100', '101', '110', '111', '1000', \
                                                 '1001', '1010', '1011', '1100', '1101', '1110', '1111', \
                                                 '10000', '10001', '10010', '10011', '10100', '10101', \
                                                 '10110', '10111', '11000', '11001', '11010', '11011', \
                                                 '11100', '11101', '11110', '11111'])

def test_binary_32():
    assert generate_binary_numbers(32) == Queue(['1', '10', '11', '100', '101', '110', '111', '1000', \
                                                 '1001', '1010', '1011', '1100', '1101', '1110', '1111', \
                                                 '10000', '10001', '10010', '10011', '10100', '10101', \
                                                 '10110', '10111', '11000', '11001', '11010', '11011', \
                                                 '11100', '11101', '11110', '11111', '100000'])

def test_binary_33():
    assert generate_binary_numbers(33) == Queue(['1', '10', '11', '100', '101', '110', '111', '1000', \
                                                 '1001', '1010', '1011', '1100', '1101', '1110', '1111', \
                                                 '10000', '10001', '10010', '10011', '10100', '10101', \
                                                 '10110', '10111', '11000', '11001', '11010', '11011', \
                                                 '11100', '11101', '11110', '11111', '100000', '100001'])

