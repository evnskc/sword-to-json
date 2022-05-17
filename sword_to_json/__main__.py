import argparse
import importlib.metadata
import json
import os

import sword_to_json
from sword_to_json.books_from_sword import generate_books

metadata = importlib.metadata.metadata(sword_to_json.__name__)

parser = argparse.ArgumentParser()
parser.add_argument('sword', help="path to zipped sword module")
parser.add_argument('module', help="name of the sword module to load")
parser.add_argument('--output', '-o', help="path to write generated JSON file")
parser.add_argument('--version', '-v', action='version', version=f"{metadata['name']} {metadata['version']}")

args = parser.parse_args()

if args.output is None:
    args.output = f"{os.path.dirname(args.sword)}/{args.module}.json"


def main():
    with open(args.output, 'w') as outfile:
        json.dump(generate_books(args.sword, args.module), outfile)


main()
