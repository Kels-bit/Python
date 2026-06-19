from pathlib import Path



path = Path('../text_files/guest_book.txt')

prompt = "\nEnter 'quit to exit program:"
prompt += "\nEnter a name: "

guest_name = ""
guest_list = ""

while guest_name != 'quit':
    guest_name = input(prompt)

    if guest_name != 'quit':
        guest_list += f"{guest_name}\n"

path.write_text(guest_list)
readme = path.read_text().rstrip()
print(readme)
