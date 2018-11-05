# Week11, Example12

import json
import datetime

# Create a class, which is a subclass of JSONDecoder.
class PersonDecoder(json.JSONDecoder):
    # Make new instances of the PersonDecoder be custom
    # versions of the default JSONDecoder, adding in an object
    # hook, which is the object_hook function defined in this class
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    # This gets run on each object
    def object_hook(self, obj):
        # If we don't have the _type entry in the JSON object,
        # then we don't need to do anything special
        if '_type' not in obj:
            return obj
        else:
            type = obj['_type']
            if type == 'date':
                # MAGIC !
                return datetime.datetime.strptime(obj['value'], "%Y-%m-%d").date()

# Create a class, which is a subclass of JSONEncoder.
class PersonEncoder(json.JSONEncoder):
    # Modify the default behaviour. This function is called
    # on each element in the object being decoded, in this
    # case it is being called twice, once for the name string,
    # and then again for the dob date.
    def default(self, obj):
        # If the thing is a date, do something custom !
        if isinstance(obj, datetime.date):
            # Return a dictionary.
            return {
                # This is so our Decoder knows what to do.
                # It is customary to start metadata like this
                # with an underscore.
                "_type": "date",
                "value": obj.isoformat()
                }
        # And if this isn't a date, just return what
        # we would do without this custom encoder.
        else:
            return super(PersonEncoder, self).default(obj)

person = {
    "name": "Albert Einstien",
    "dob": datetime.date(year=1879, month=3, day=14)
}

# Write this to the file.
print(json.dumps(person, cls=PersonEncoder))
with open("albert.txt", "w") as outfile:
    json.dump(person, outfile, cls=PersonEncoder)
with open("albert.txt", "r") as infile:
    person2 = json.load(infile, cls=PersonDecoder)

print(person)
print(person2)
if person == person2:
    print("I saved and then loaded, and I got the same person !")