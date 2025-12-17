#dictionary(key:value pairs)  Unique

dict = {
    "name":"sravan kumar",
    "subject" : "AI & ML",
    "status" : "beginner"
}
print(dict)
print(type(dict))
print(dict["name"])

#methods

print(dict.keys())

print(dict.values())

print(dict.items())

print(dict.get("status"))

dict.update({
    "city" : "hyderabad"
    })