
def count_words(string):
    words = string.split()
    return len(words)

def get_chars_dict(string):
    lowercase_string = string.lower()
    chars_Dict = {}

    for character in lowercase_string:
        if character in chars_Dict:
            chars_Dict[character] += 1
        else:
            chars_Dict[character] = 1

    return chars_Dict



def chars_dict_to_sorted_list(character_dict):
    def sort_on(dict):
        return dict["count"]
    character_list = []
    
    for item in character_dict:
        if item.isalpha():
            character_list.append({"character": item, "count": character_dict[item]})
    
    character_list.sort(reverse=True, key=sort_on)

    return character_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
def print_report(book, string):
    words = count_words(string)
    chars_dict = get_chars_dict(string)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print("")
    for item in sorted_chars_list:
        character = item["character"]
        count = item["count"]
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

def main():
        book_path = "books/frankenstein.txt"
        book_text = get_book_text(book_path)
        print_report(book_path,book_text)

main()

