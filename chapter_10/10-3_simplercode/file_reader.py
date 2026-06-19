from pathlib import Path

path = Path('../text_files/pi_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line    

print(pi_string)
print(len(pi_string))
