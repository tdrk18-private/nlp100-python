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
