# Week11, Example11

import json
import datetime

# Create a class, which is a subclass of JSONEncoder.
class PersonEncoder(json.JSONEncoder):
    # Modify the default behaviour. This function is called
    # on each element in the object being encoded, in this
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

print(json.dumps(person, cls=PersonEncoder))
with open("albert.txt", "w") as outfile:
    json.dump(person, outfile, cls=PersonEncoder)