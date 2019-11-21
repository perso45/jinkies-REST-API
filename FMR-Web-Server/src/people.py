#System modules
from datetime import datetime
#Extra modules
from flask import make_response,abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
#Data to present to our API
PEOPLE = {
    "Holden":{
        "fname":"Ethan",
        "lname":"Holden",
        "timestamp":get_timestamp()
    },
    "Claus":{
        "fname":"Santa",
        "lname":"Claus",
        "timestamp":get_timestamp()
    },
    "Gates":{
        "fname":"Bill",
        "lname":"Gates",
        "timestamp":get_timestamp()
    }
}
#Create handler for read/GET people
def read_all():
    #Responds to /api/people request with a list of people
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    #Checks if person is present in list
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with {lname} not found".format(lname=lname)
        )
    return person

def create(person):
    lname = person.get("lname",None)
    fname = person.get("fname",None)
    #Checks if person exists
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
        "lname":lname,
        "fname":fname,
        "timestamp":get_timestamp(),
        }
        return make_response("{lname} has been successfully created".format(lname=lname),201)
    else:
        abort(
            406, "This last name {lname} already exists".format(lname=lname)
        )
def update(lname,person):
    #Does person exist
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, "Last name {lname} not found".format(lname=lname)
        )

def delete(lname):
    #Does person exist
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname),200
        )
    else:
        abort(
            404, "Last name {lname} not found".format(lname=lname)
        )
