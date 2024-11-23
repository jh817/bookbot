def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()  
        book = file_contents.split()

    def get_word_count():
        print(f"There are {len(book)} words found in this document")
    
    def get_char_count():
        char_count = {}
        lowered_book = file_contents.lower()
        for b in lowered_book: 
            if b.isalpha():
                if b in char_count:
                    char_count[b] += 1   
                else: char_count[b] = 1
        print("")
        char_count = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
        for k, v in char_count:
           print(f"The '{k}' character was found {v} times")

    print(f"--- Begin report of {book_path} ---")
    get_word_count()
    get_char_count()

main()