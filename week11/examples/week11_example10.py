# Week11, Example10

import json
import datetime

person = {
    "name": "Albert Einstien",
    "dob": datetime.date(year=1879, month=3, day=14)
}

print(person["dob"].isoformat())