from pysword.modules import SwordModules

from sword_to_json.utils.progress import Progress


def generate_books(sword, module):
    modules = SwordModules(sword)
    modules.parse_modules()
    bible = modules.get_bible_from_module(module)

    book_structure = bible.get_structure().get_books()

    books = {}

    progress = Progress(sum([len(v) for v in book_structure.values()]))

    for testament, testament_books in book_structure.items():
        books[testament] = []
        for number, book in enumerate(testament_books, start=sum([len(v) for v in books.values()]) + 1):
            books[testament].append({
                "number": number,
                "name": book.name,
                "abbreviation": book.preferred_abbreviation,
                "chapters": [
                    {
                        "number": chapter,
                        "verses": [
                            {
                                "number": verse,
                                "text": bible.get(books=book.name, chapters=chapter, verses=verse).rstrip()
                            } for verse in range(1, book.chapter_lengths[chapter - 1] + 1)
                        ]
                    } for chapter in range(1, book.num_chapters + 1)
                ]
            })

            progress.update(number)

    return books
