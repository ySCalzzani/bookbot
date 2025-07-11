# python
import sys
from stats import (
        count_words,
        count_letters,
        sort_dict
        )

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    text = get_book_text(sys.argv[1]) 
    dict_text = count_letters(text)
    sorted_text = sort_dict(dict_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    count_words(text)
    print("--------- Character Count -------")
    for value in sorted_text:
        if value[0].isalpha():
            print(f"{value[0]}: {value[1]}")
    print("============= END ===============")
    return

main()

