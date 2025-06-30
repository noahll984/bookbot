import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import get_num_chars
from stats import sorted_list_of_dicts

def get_book_text():
    with open(sys.argv[1]) as f:
        print(f.read())


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    char_counts = get_num_chars()
    sorted_chars = sorted_list_of_dicts(char_counts)
    for item in sorted_chars:
        for char, count in item.items():
            print(f"{char}: {count}")
    print("============= END ===============")

main()

    
