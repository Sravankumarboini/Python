words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict = {}

for val in words:
    dict[val] = len(val)
print(dict.values())