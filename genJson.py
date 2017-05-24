import json


records = {}
records["alpha"]="gamma"
print records["alpha"]

for i in ["","",""]:
    record = {"subject":i, "items":[]}
    print records['subject']
    records.append(record)

alpha=json.dumps(records, indent=4)

for i in range(0,2):
    alpha["pickups"][0]["items"].append({"name":i, "quantity":i})


