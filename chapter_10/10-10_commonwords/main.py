from pathlib import Path


filenames = ['dracula.txt', 'thelliad.txt','theprince.txt', 'romeoandjuliet.txt']
loaded_books = []

for file in filenames:  
    try:
        path = Path("../text_files/"+(file))
        check = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"{file} was not found.")
    else:
        print(f".....{file} found.")
        loaded_books.append(file)
        

for book in loaded_books:
    path_2 = Path("../text_files/"+(book))
    read = path_2.read_text(encoding='utf-8')
    the_count = read.lower().count('the')
    thespace_count = read.lower().count('the ')
    print(f"\n{book}")
    print("-------------")
    print(f"Times 'the' appears: {the_count}")
    print(f"Times 'the ' (with a space in the string) appears: {thespace_count}")

    


