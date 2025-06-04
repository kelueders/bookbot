from stats import get_num_words, get_char_counts, convert_dict_to_sorted_list, make_report

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

if __name__ == '__main__':
    main()