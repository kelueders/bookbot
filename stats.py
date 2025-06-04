def get_num_words(text):
    num_words = len(text.split())
    return num_words

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
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter_dict in sorted_list:
        print(f"{letter_dict['letter']}: {letter_dict['num']}")
    print("============= END ===============")