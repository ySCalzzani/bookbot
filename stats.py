# python

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text: str) -> None:
    num_words = len(text.split())
    print(f'Found {num_words} total words')

def count_letters(text: str) -> dict:
    lower_text = text.lower()
    counter = {}
    for letter in lower_text:
        counter[letter] = counter.get(letter, 0) + 1
   
    return counter

def sort_dict(contents:dict) -> dict:
    sorted_content = sorted(
            contents.items(),
            key=lambda item: item
            )
    return sorted_content
   
