info = [
    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english")
]

dict = {}
course_set = set()
for tup in info :
    course_set.add(tup[1]) #course
    if(tup[1] == "english"):
        print(tup[0])
    
    if(dict.get(tup[0])== None) :
        dict.update({tup[0]:set()})
        dict[tup[0]].add(tup[1])
    else:
        dict[tup[0]].add(tup[1])
    

print(course_set)
print(dict)