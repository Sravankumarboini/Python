#Basics of python
'''
Multi line comment
'''
name = "Sravan"
age = 21
PI = 3.14

print("my name is :", name)
print("my age is :", age)

print(type(name),type(age),type(PI))

full_name = "Boini Sravan kumar"

print(full_name)

a=5
b=10

sum=a+b 
print("sum :",sum)

#operators
#arithmetic
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#relational operator
print(a<b)
print(a>=b)
print(a!=b)
print(a==b)

#Assignment operator(=,+=,-=,*=,/=)
a=b 

#logical operator(not(!) , and(&&) , or(||))

var = False

print(not var)
print(a>b and b>a)
print(a>b or b>a)

#Type Conversion(implicit(done by compiler))

print(a/b) #implicitly cpnverting to float

#Type Casting(Explicit)(int(), bool(), float())

c=int(PI)
print(c)

#input(by default String)

d = int(input("Enter value of d :"))

e = int(input("Enter value of e :"))
print(d+e)