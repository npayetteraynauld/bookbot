def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(path):
    book_text = get_book_text(path)
    words = book_text.split()
    return len(words) 

def get_char_count(path):
    char_dictionary = {}
    book_string = get_book_text(path)
    for char in book_string:
        char = char.lower()
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary

def sorted_chars(dic):
    sorted_list = dict(sorted(dic.items(),key=get_value, reverse=True))
    return sorted_list 

def get_value(item):
    return item[1]

def common_word(path):
    word_dictionary = {}
    words = get_book_text(path).split()
    for word in words:
        word = word.lower()
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return word_dictionary 

def sorted_common_word():
    dic = common_word("books/frankenstein.txt")
    sorted_dic = dict(sorted(dic.items(), key=lambda item : item[1], reverse = True))
    print(sorted_dic)

sorted_common_word() 
