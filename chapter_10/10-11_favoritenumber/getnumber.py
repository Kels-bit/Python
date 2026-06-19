from pathlib import Path
import json



path = Path('../text_files/numbers.json')
favorite_number = input("What is your favorite number? ")
store_number = json.dumps(favorite_number)
path.write_text(store_number)


