import json
stuff='''
{ 
    "Name":"Jambo",
    "Phone":{
        "Type":"Mobile",
        "Number":"Unknown"
        },
    "ID":"No ID"
}'''
data=json.loads(stuff)
print("Name: " ,data["Name"])
print("ID: " ,data["ID"])
print("Number: " ,data["Phone"]["Number"])
print(" ")


Info='''
[
    {
    "Name":"person 2",
    "Phone":{
        "Type":"Mobile",
        "Number":"03006860304"
        },
    "ID":"001"
    },
    {
    "Name":"person 1",
    "Phone":{
        "Type":"Mobile",
        "Number":"03002779689"
        },
    "ID":"002"
    }
]'''
lst=json.loads(Info)
for data in lst:
    print("Name: " ,data["Name"])
    print("ID: " ,data["ID"])
    print("Number: " ,data["Phone"]["Number"])
    print(" ")
