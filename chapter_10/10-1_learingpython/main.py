from pathlib import Path

path = Path('../text_files/learning_python.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()

text_string = ''
for line in lines:
    print("/n")
    text_string += line
    


#Output
print(contents)
print(text_string)


