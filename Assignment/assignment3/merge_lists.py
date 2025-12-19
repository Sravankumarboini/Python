n = int(input("enter list_1 size : "))
list1 = []
for i in range(n):
    list1.append(input("enter element:"))

m = int(input("enter list_2 size : "))
list2 = []
for i in range(m):
    list2.append(input("enter element:"))

for i in range(m):
    list1.append(list2[i])

list1.sort()
print(list1)