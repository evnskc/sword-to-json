from sword_to_json import __main__


def test_generate_dict(sword, module, name, abbreviation):
    bible_dict = __main__.generate_dict(sword, module, name, abbreviation)
    assert all((
        bible_dict["name"] == name,
        bible_dict["abbreviation"] == abbreviation,
        len(bible_dict["books"]) == 66
    ))
