from pathlib import Path


filenames = ['gerbil.txt', 'cats.txt', 'fish.txt', 'dogs.txt']
print("\n")

for file in filenames:
    try:
        path = Path("../text_files/"+(file))
        names = path.read_text(encoding='utf-8') #Added encoding agrument to run on other computers.
    except FileNotFoundError:
        print(f"The file {file} is missing.\n")
    else:
        print(f"Names in {file}:")
        print('--------------------')
        print(names)

