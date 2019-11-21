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
        "bdate":"06/12/2003",
        "timestamp":get_timestamp()
    },
    "Claus":{
        "fname":"Santa",
        "lname":"Claus",
        "bdate":"03/15/0475",
        "timestamp":get_timestamp()
    },
    "Gates":{
        "fname":"Bill",
        "lname":"Gates",
        "bdate":"10/28/1955",
        "timestamp":get_timestamp()
    }
}
#Create handler for read/GET people
def read_all():
    #Responds to /api/people request with a list of people
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(fname,lname):
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
    bdate = person.get("bdate",None)
    #Checks if person exists
    if lname and fname not in PEOPLE and lname and fname is not None:
        PEOPLE[fname + lname] = {
        "lname":lname,
        "fname":fname,
        "bdate":bdate,
        "timestamp":get_timestamp(),
        }
        return make_response("User has been successfully created",201)
    else:
        abort(
            406, "This name already exists"
        )
def update(fname,lname,person):
    #Does person exist
    if lname and fname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, "Last name {lname} not found".format(lname=lname)
        )

def delete(fname,lname):
    #Does person exist
    if lname and fname in PEOPLE:
        del PEOPLE[fname + lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname),200
        )
    else:
        abort(
            404, "Last name {lname} not found".format(lname=lname)
        )
