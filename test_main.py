from main import check_character, space_printer, fill_answer


def test_check_character():
    assert check_character("d", "dinosaur") is True
    assert check_character("d", "scream") is False

def test_space_printer():
    assert space_printer("hello") == "_ _ _ _ _ "
    assert space_printer("h") == "_ "
    assert space_printer("extremely") == "_ _ _ _ _ _ _ _ _ "


