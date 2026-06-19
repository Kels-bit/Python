from pathlib import Path
from functions.shownum import show_number as sn
import json

def get_number():
    path = Path('../text_files/numbers.json')
    if path.exists():
        sn()
    else:
        fav_num = input("What is your favorite number? ")
        load = json.dumps(fav_num)
        path.write_text(load)
        #Use show number function
        sn()

