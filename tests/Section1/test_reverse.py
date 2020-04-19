from Section1.reverse import Section1


def test_reverse():
    result = Section1.reverse("stressed")
    assert result == "desserts"
