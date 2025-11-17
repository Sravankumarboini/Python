i = 1
while i<=5:
    print(i)
    i+=1

#multiplication table
'''
n = int(input("enter the number : "))

i=1

while i<=10 :
    print(n,"*",i,"=",n*i)
    i+=1
'''

#for loop

string = "hello"

#in -> membership operator(to check presence)

for i in string:
    print(i)


word = "artificial intelligence"
ans=0

for ch in word :
    if(ch== 'a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        ans+=1
print("vowel count is :", ans)



print("sum of n natural numbers")

n=int(input("enter input: "))
sum=0
for i in range(n+1):
    sum+=i
print("sum is: ",sum)
