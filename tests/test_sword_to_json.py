from jsonschema import validate

from sword_to_json.books_from_sword import generate_books


def test_sword_to_json(sword, module):
    books = generate_books(sword, module)

    book_schema = {
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

    schema = {
        "type": "object",
        "properties": {
            "ot": {
                "type": "array",
                "uniqueItems": True,
                "maxItems": 39,
                "minItems": 39,
                "items": book_schema
            },
            "nt": {
                "type": "array",
                "uniqueItems": True,
                "maxItems": 27,
                "minItems": 27,
                "items": book_schema
            }
        }
    }

    validate(books, schema)
