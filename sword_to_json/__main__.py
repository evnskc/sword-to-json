import argparse
import json
import os

from sword_to_json.books_from_sword import generate_books

parser = argparse.ArgumentParser("Generate JSON Files from SWORD Modules")
parser.add_argument('sword', help="path to zipped sword module")
parser.add_argument('module', help="name of the sword module to load")
parser.add_argument('--output', '-o', help="path to write generated JSON file")

args = parser.parse_args()

if args.output is None:
    args.output = f"{os.path.dirname(args.sword)}/{args.module}.json"

with open(args.output, 'w') as outfile:
    json.dump(generate_books(args.sword, args.module), outfile)
