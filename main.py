import sys

from stats import get_characters_sorted, get_text_words


def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    book_text = get_book_text(path)
    num_words = get_text_words(book_text)
    num_chars = get_characters_sorted(book_text)
    report = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{num_chars}
============= END ==============="""
    print(report)


main()
