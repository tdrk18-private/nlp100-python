from Section1.section1 import Section1


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
