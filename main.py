import json
from datetime import date

todays = date.today()
todays = str(todays)
inputt = str(input(""))

inp = {
    todays: {
        "entry": inputt
    }
}

f = open("todo.json", "a")
json.dump(inp, f)