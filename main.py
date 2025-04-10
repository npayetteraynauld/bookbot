from stats import get_word_count, get_char_count, sorted_chars 
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        path = sys.argv[1]
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        word_count = get_word_count(path)
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        char_count = get_char_count(path)
    
        sorted_dic = sorted_chars(char_count)
        for key, value in sorted_dic.items():
            if key.isalpha():
                print(f"{key}: {value}")
        print("============= END ===============")
     
main()
