import sys

from stats import get_book_text

from stats import get_book_text_count

from stats import get_character_count

from stats import get_sorted_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    word_number = get_book_text_count(text)
    character_count = get_character_count(text)
    sorted_list = get_sorted_count(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_number} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()