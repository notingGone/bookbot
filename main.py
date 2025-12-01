#!/usr/bin/env python3

import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(list):
    for item in list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = count_characters(text)
    print_report(sort_characters(character_count))

main()
