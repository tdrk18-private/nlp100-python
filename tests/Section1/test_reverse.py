from Section1.reverse import Section1


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
