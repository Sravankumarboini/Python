list1 = [int(input()) for i in range(int(input("enter the length:")))]
set1 = set()

for val in list1:
    if val in set1:
        print(val)
    set1.add(val)