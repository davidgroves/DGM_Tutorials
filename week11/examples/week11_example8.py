# Week11, Example8

import json

with open("week11_example8.json") as jf:
    president = json.load(jf)
    print(type(president))
    print(f"This presidents first name is {president['Firstname']}")
    termcount = len(president["Terms"])
    print(f"This president served {termcount} terms")
    