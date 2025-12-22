f = open("text.txt", "r") #file object
data = f.read()

print(data)
print(type(data))
print(type(f))

f.seek(0)

data1 = f.readline() #it will read line by line

print(data1)

f.write("Text to override \n the complete data.")

f.close()