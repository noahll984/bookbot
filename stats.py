import sys

def get_num_words():
    with open(sys.argv[1]) as f:
        num_words = len(f.read().split())
        print(f"Found {num_words} total words")


def get_num_chars():
    char_counts = {}
    with open(sys.argv[1]) as f:
        text = f.read().lower()
        for char in text:
                char_counts[char] = char_counts.get(char, 0) + 1
        return char_counts     

def sorted_list_of_dicts(char_counts):
    sorted_chars = sorted(char_counts, key=char_counts.get, reverse=True)
    sorted_list = []
    for char in sorted_chars:
        sorted_list.append({char: char_counts[char]})
    return sorted_list

