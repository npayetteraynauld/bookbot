def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count():
    book_text = get_book_text("books/frankenstein.txt")
    words = book_text.split()
    counter = 0
    for word in words: 
        counter += 1
    return counter
