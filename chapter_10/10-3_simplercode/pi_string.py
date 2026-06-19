from pathlib import Path
path = Path('../text_files/pi_digits.txt')
contents = path.read_text().rstrip()   # You get rid of the temp variable by method chaining.
print(contents)
