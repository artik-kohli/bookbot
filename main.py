import sys
from stats import word_count, get_character_count, get_sorted_dict_list

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text("books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    file_path = sys.argv[1]
    chars = get_character_count(get_book_text(file_path))
    chars = get_sorted_dict_list(chars)
    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()