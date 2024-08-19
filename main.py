def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    return len(text.split())


def character_count(text):
    # Count the number of occurrences of each character in the text
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    # Convert the dictionary to a list of dictionaries
    result = [{"char": key, "count": value} for key, value in char_dict.items()]
    return result


def print_report(doc_path, word_count, char_count):
    print(f"--- Begin report of {doc_path} ---")
    print(f"{word_count} words found in the document\n")

    def sort_on(dict):
        return dict["count"]

    char_count.sort(key=sort_on, reverse=True)
    for char in char_count:
        print(f"The '{char['char']}' character was found {char['count']} times")

    print("--- End report ---")


if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    book = read_book(book_path)
    word_count = count_words(book)
    char_count = character_count(book)
    print_report(book_path, word_count, char_count)
