from pathlib import Path

path = Path('../text_files/learning_python.txt')

contents = path.read_text().rstrip()
#Display contents before the replacement of a new word.
print(contents)

#Replace the desired word.
contents = contents.replace('Python', 'C')

print(contents)

