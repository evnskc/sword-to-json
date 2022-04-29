from jsonschema import validate
from sword_to_json.books_from_sword import generate_books


def test_sword_to_json(sword, module):
    books = generate_books(sword, module)

    schema = {
        "type": "array",
        "uniqueItems": True,
        "maxItems": 66,
        "minItems": 66,
        "items": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "minimum": 1},
                "name": {"type": "string"},
                "abbreviation": {"type": "string"},
                "chapters": {
                    "type": "array",
                    "uniqueItems": True,
                    "items": {
                        "type": "object",
                        "properties": {
                            "number": {"type": "integer", "minimum": 1},
                            "verses": {
                                "type": "array",
                                "uniqueItems": True,
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "number": {"type": "integer", "minimum": 1},
                                        "text": {"type": "string"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    validate(books, schema)
