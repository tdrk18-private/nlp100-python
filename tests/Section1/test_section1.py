from Section1.section1 import Section1, NGramType


def test_reverse():
    result = Section1.reverse("stressed")
    assert result == "desserts"


def test_extract_odd():
    result = Section1.extract_odd("パタトクカシーー")
    assert result == "パトカー"


def test_merge_string():
    result = Section1.merge_strings("パトカー", "タクシー")
    assert result == "パタトクカシーー"


def test_pi_list():
    text = "Now I need a drink, alcoholic of course, " \
           "after the heavy lectures involving quantum mechanics."
    result = Section1.pi_list(text)
    assert result == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


def test_element_symbol():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
           "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    result = Section1.element_symbol(text, [1, 5, 6, 7, 8, 9, 15, 16, 19])
    assert result == {
        "Be": 4, "C": 6, "B": 5, "Ca": 20, "F": 9, "S": 16, "H": 1,
        "K": 19, "Al": 13, "Mi": 12, "Ne": 10, "O": 8, "Li": 3, "P": 15,
        "Si": 14, "Ar": 18, "Na": 11, "N": 7, "Cl": 17, "He": 2
    }


def test_n_gram():
    text = "I am an NLPer"
    c_gram = Section1.n_gram(text, 2, NGramType.CHAR)
    w_gram = Section1.n_gram(text, 2, NGramType.WORD)
    assert c_gram == ["Ia", "am", "ma", "an", "nN", "NL", "LP", "Pe", "er"]
    assert w_gram == ["I am", "am an", "an NLPer"]


def test_set():
    text_x = "paraparaparadise"
    text_y = "paragraph"
    x = Section1.n_gram(text_x, 2, NGramType.CHAR)
    y = Section1.n_gram(text_y, 2, NGramType.CHAR)
    union = Section1.union(x, y)
    assert union == {"pa", "ar", "ra", "ap", "ad", "di", "is", "se", "ag", "gr", "ph"}
    intersection = Section1.intersection(x, y)
    assert intersection == {"pa", "ar", "ra", "ap"}
    set_difference = Section1.set_difference(x, y)
    assert set_difference == {"ad", "di", "is", "se"}
    includes_x = "se" in x
    includes_y = "se" in y
    assert includes_x
    assert not includes_y


def test_template():
    result = Section1.template(12, "気温", 22.4)
    assert result == "12時の気温は22.4"


def test_cipher():
    x = "re1Ae"
    encrypt = Section1.cipher(x)
    assert encrypt == "iv1Av"
    decrypt = Section1.cipher(encrypt)
    assert decrypt == "re1Ae"
