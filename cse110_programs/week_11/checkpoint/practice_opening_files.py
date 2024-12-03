# Example of printing files from a folder

with open("books.txt") as file:
    for line in book_file:
        # Strips hidden \n from file
        book = line.strip()
        print(books)