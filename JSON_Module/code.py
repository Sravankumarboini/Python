import json

json_str = '{"name": "sravan kumar", "isStudent": true}'

py_obj = json.loads(json_str)#converts json str to python object

print(type(py_obj), py_obj)

json_str1 = json.dumps(py_obj)#converts python object to json string

print(type(json_str1), json_str1)