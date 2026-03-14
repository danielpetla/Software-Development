import vowels


def test_vowels_simple():
    assert vowels.vowels("abcabc") == {"a"}

def test_vowels_repeat():
    assert vowels.vowels("aaaaa") == {"a"}

