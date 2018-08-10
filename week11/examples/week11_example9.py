# Week11, Example9

import json
import datetime

shape = {
    "name": "Cuboid",
    "height": 30,
    "width": 20,
    "length": 15
}

person = {
    "name": "Albert Einstien",
    "dob": datetime.date(year=1879, month=3, day=14)
}

print(json.dumps(shape))
print(json.dumps(person))
