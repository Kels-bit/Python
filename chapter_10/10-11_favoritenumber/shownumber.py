from pathlib import Path
import json



path = Path('../text_files/numbers.json')
show_number = path.read_text()
fav_num = json.loads(show_number)

print(f"Your favorite number is: {fav_num}")
