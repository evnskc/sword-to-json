import argparse
import json
from pathlib import Path

from sword_to_json.books_from_sword import generate_books
from utils import metadata


def main():
    parser = argparse.ArgumentParser(description=metadata.summary)
    parser.add_argument("sword", help="path to zipped sword module")
    parser.add_argument("module", help="name of the sword module to load")
    parser.add_argument("-o", "--output", help="path to write generated JSON file")
    parser.add_argument("-v", "--version", action="version", version=f"{metadata.name} {metadata.version}")

    args = parser.parse_args()

    if args.output is None:
        args.output = f"{Path(args.sword).resolve().parent}/{args.module}.json"

    with open(args.output, "w") as outfile:
        json.dump({"books": generate_books(args.sword, args.module)}, outfile)


if __name__ == "__main__":
    main()
