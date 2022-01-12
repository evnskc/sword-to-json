import argparse
import json
import os
from itertools import chain

from pysword.modules import SwordModules


def generate_dict(sword, module, name, abbreviation):
    modules = SwordModules(sword)
    modules.parse_modules()
    bible = modules.get_bible_from_module(module)

    bible_dict = {
        "name": name,
        "abbreviation": abbreviation,
        "books": []
    }

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
        bible_dict["books"].append({
            "number": book_number,
            "name": book.name,
            "abbreviation": book.preferred_abbreviation,
            "chapters": chapters,
        })
    return bible_dict


def main():
    parser = argparse.ArgumentParser("Generate JSON Files from SWORD Modules")
    parser.add_argument('sword', help="path to zipped sword module")
    parser.add_argument('module', help="name of the sword module to load")
    parser.add_argument('--name', '-n', help="name of the Bible translation", default="")
    parser.add_argument('--abbreviation', '-a', help="abbreviation of the Bible translation", default="")
    parser.add_argument('--output', '-o', help="path to write generated JSON file")

    args = parser.parse_args()

    if args.output is None:
        args.output = f"{os.path.dirname(args.sword)}/{args.module}.json"

    with open(args.output, 'w') as outfile:
        json.dump(generate_dict(args.sword, args.module, args.name, args.abbreviation), outfile)


if __name__ == "__main__":
    main()
