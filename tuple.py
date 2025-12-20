#tuple(immutable sequence of values)

tuple = (1,2,3,4,5)

print(tuple)
print(len(tuple))

print(tuple[3:])

sum=0

for val in tuple:
    sum+=val
print(sum)

#index method(return first occurence idx)

print(tuple.index(2))

#count the value occurences

print(tuple.count(10))