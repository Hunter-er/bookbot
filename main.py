from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    test_book = sys.argv[1]
    #test_book = "books/frankenstein.txt"
    book_text = get_book_text(test_book)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars_list = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {test_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_chars_list:
        print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

    