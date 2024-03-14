# TEST FILE FOR MATCHER
# DO NOT MODIFY
from matching import matcher

def test_matcher_pass_solo1():
    assert matcher("[ ]") == True

def test_matcher_pass_solo2():
    assert matcher("{ }") == True

def test_matcher_pass_none():
    assert matcher("hello") == True

def test_matcher_pass_arith():
    assert matcher("(45 + 36) - 5") == True

def test_matcher_pass_mix2():
    assert matcher("[()]") == True

def test_matcher_pass_mix3():
    assert matcher("{[()]}") == True

def test_matcher_pass_mix5():
    assert matcher("{ () [ [] ( {} ) ] }") == True

def test_matcher_pass_mix_lots():
    assert matcher("{[()]} [ ] ( ) ([{}]) { () [ [] ( {} ) ] } ( {[()] [] } {} )") == True

def test_matcher_pass_mix():
    assert matcher("map{key[a(4)]}{b([v])}") == True

def test_matcher_pass_paren():
    assert matcher("map(ke(a(4)))(b((v)))") == True

def test_matcher_fail_paren():
    assert matcher("( ( a )") == False

def test_matcher_fail_mix():
    assert matcher("({)}") == False

def test_matcher_fail_mix2():
    assert matcher("[(])") == False

def test_matcher_fail_mix3():
    assert matcher("{[(})]") == False

def test_matcher_fail_mix4():
    assert matcher("({)") == False

def test_matcher_fail_mix5():
    assert matcher("[(]") == False

def test_matcher_fail_mix6():
    assert matcher("{[(})") == False

def test_matcher_fail_mix7():
    assert matcher("{[(])}") == False

def test_matcher_fail_mix8():
    assert matcher("{[()}()]") == False


def test_matcher_fail_back_paren():
    assert matcher("))((") == False

def test_matcher_fail_uneven_paren():
    assert matcher("(a)b)") == False

def test_matcher_fail_back_mix():
    assert matcher("]){(") == False

def test_matcher_fail_back_mix2():
    assert matcher("])[(") == False

def test_matcher_fail_uneven_mix():
    assert matcher("(a)b}") == False

def test_matcher_fail_uneven_mix2():
    assert matcher("a[b]{") == False