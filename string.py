#string is immmutable
name = "sravan"

print(len(name))

#conactinate

print(name + "kumar")

#slicing
#str[st idx : end idx] ending index is not inclluded

print(name[2:4])
print(name[-4:-2])

#string formatting(format and f-string)

#format 
#normal formatting
print("sum of {} & {} is {}".format(10,15,25))
#index based formatting
print("sum of {1} & {0} is {2}".format(10,15,25))
#value based formatting
print("values of a= {a} & b={b}".format(a=5,b=10))

