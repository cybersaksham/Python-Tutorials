import json

data = '{"var1":"saksham","var2":"harry"}'

parsed = json.loads(data)  # Parsing a json data
print(f"data = {data}")
print(f"parsed = {parsed}")
print(type(parsed))
print(f"parsed['var1'] = {parsed['var1']}")

# json.load --> load a json file

data2 = {"name": "saksham",
         "cars": ['bmw', 'ferrari', 'audi'],
         "fridge": ('roti', 'chawal'),
         "isbad": False}
# This data can be used in python but tuple & list are not defined in javascript so it will not work there
jscomp = json.dumps(data2)  # This converts python file to java
print(jscomp)

jscomp2 = json.dumps(data2, sort_keys=True)  # sort_keys parameter sort all data if given True
print(jscomp2)
