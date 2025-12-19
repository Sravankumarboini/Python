n = int(input("Enter number of elements: "))
lst = []

sum=0
for i in range(n):
    item = int(input("Enter element: "))
    lst.append(item)
    sum+=item
print("Average of the list is :", sum/len(lst))
