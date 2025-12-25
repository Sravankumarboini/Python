n = int(input("enter the length of list1 :"))
list1 = []
list2 = []

for i in range(n):
    list1.append(int(input()))

m = int(input("eneter the length of list2 :"))

for i in range(m):
    list2.append(int(input()))

set1 = set()

for val in list1:
    set1.add(val)

flag =  False
for val in list2:
    if val in set1:
        flag = True 
        break

if(flag) :
    print("share common element")
else:
    print("no common element")