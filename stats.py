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
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {doc_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_count.sort(key=lambda x: x["count"], reverse=True)
    for char in char_count:
        print(f"{char['char']}: {char['count']}")

    print("============= END ===============")
