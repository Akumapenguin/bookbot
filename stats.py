import string

def get_book_text(PATH):
    with open(PATH) as f:
        file_contents = f.read()  
        return file_contents

def get_book_text_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_character_count(book_text):
    character_list = book_text.lower()
    char_count = {}
    for char in character_list:
        if char in string.punctuation or char in string.whitespace:
            continue

        char_count[char] = char_count.get(char,0) + 1
    return char_count
    
def get_sorted_count(character_count):
    character_list = sorted(character_count.items(), key=lambda character: character[1], reverse = True)
    return (character_list)