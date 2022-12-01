"""Testing our Newick parser."""

from newick import parse, tokenize, Tree



def test_me() -> None:
    """Test what you need to test."""
    assert 2 + 2 == 4
    assert tokenize("(A, (B, C))") == ['(', 'A', '(', 'B', 'C', ')', ')']

    assert str(parse("(A, (B, C))")) == ('(A,(B,C))')
    assert str(parse("((A,B), (C,D), E)")) == '((A,B),(C,D),E)'
    assert str(parse("((A,(B,C)), (D,E), F)")) == '((A,(B,C)),(D,E),F)'
    assert str(parse("((A,(B,C)), (D,E), F)")) == '((A,(B,C)),(D,E),F)'
    assert str(parse("(A, (B, C), (D,(E,F)), (G,(H,(I,J))))")) == '(A,(B,C),(D,(E,F)),(G,(H,(I,J))))'