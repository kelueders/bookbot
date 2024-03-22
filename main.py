def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_counts(text)
    dict_list = convert_dict_to_sorted_list(char_count)
    make_report(book_path, num_words, dict_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict['num']

def convert_dict_to_sorted_list(dict):
    dict_list = []
    for k, v in dict.items():
        my_dict = {}
        my_dict['letter'] = k
        my_dict['num'] = v
        dict_list.append(my_dict)
        dict_list.sort(reverse=True, key=sort_on)    # sort() method sorts the list in place and returns None, not a new sorted list

    return dict_list

def make_report(path, num_words, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"There are {num_words} words in the document")
    print()
    for letter_dict in sorted_list:
        print(f"The '{letter_dict['letter']}' character was found {letter_dict['num']} times")
    print("--- End report ---")

if __name__ == '__main__':
    main()