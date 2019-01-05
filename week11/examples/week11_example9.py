# Week11, Example9

import json
import datetime

person = {
    "name": "Albert Einstien",
    "dob": datetime.date(year=1879, month=3, day=14)
}

print(json.dumps(person))