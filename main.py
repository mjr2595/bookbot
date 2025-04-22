import sys

from stats import character_count, count_words, print_report, read_book

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = read_book(book_path)
    word_count = count_words(book)
    char_count = character_count(book)
    print_report(book_path, word_count, char_count)
