from pathlib import Path
import json


def show_number():
    path = Path('../text_files/numbers.json')
    find_number = path.read_text()
    fav_num = json.loads(find_number)
    print(f"Your favorite number is: {fav_num}")
