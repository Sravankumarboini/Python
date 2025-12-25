string = input("enter the string: ")

cnt = 0

for i in range (len(string)):
    if(string[i] == " "):
        cnt += 1
print(cnt)