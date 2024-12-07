# This program tries to find items in a file in a parallel list
# Patrick T. Edgett
# 12/4/24

largest_chapter = 0
largest_book = ""

mormon_largest_chapter = 0
mormon_largest_book = ""

with open("books_and_chapters.txt") as file:
    user = input("Which Book do You want to look at? ").lower()
    
    for line in file:
        parts = line.split(":")
        book = parts[0].strip()
        chapter = int(parts[1])
        scripture = parts[2].strip()

        if scripture.lower() == user:
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
    
        # Find the Largest Chapter Overall
        if chapter > largest_chapter:
            largest_chapter = chapter
            largest_book = book

        # Find the Largest Chapter in the Book of Mormon
        if chapter > mormon_largest_chapter and scripture == "Book of Mormon":
            mormon_largest_chapter = chapter
            mormon_largest_book = book

    print()
    print(f"The Largest Number of Chapters is '{largest_chapter}' in '{largest_book}'")
    print(f"The Largest Book in The Book of Mormon is: {mormon_largest_book} with '{mormon_largest_chapter}' chapters")
    
