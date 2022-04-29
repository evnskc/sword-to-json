from itertools import chain
from pysword.modules import SwordModules


def generate_books(sword, module):
    modules = SwordModules(sword)
    modules.parse_modules()
    bible = modules.get_bible_from_module(module)

    books = []

    for book_number, book in enumerate((*chain(*bible.get_structure().get_books().values()),), 1):
        chapters = []
        for chapter_number in range(1, book.num_chapters + 1):
            verses = []
            for verse_number in range(1, len(book.get_indicies(chapter_number)) + 1):
                verses.append({
                    "number": verse_number,
                    "text": bible.get(books=[book.name], chapters=[chapter_number], verses=[verse_number])
                })
            chapters.append({
                "number": chapter_number,
                "verses": verses
            })
        books.append({
            "number": book_number,
            "name": book.name,
            "abbreviation": book.preferred_abbreviation,
            "chapters": chapters,
        })

    return books
