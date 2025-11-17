def func(a,b,c):
    s=(a+b+c)/3
    return s

print(func(3,4,5))

#lambda funtions

sum=lambda a,b : a+b

print(sum(4,5))

#factorial of n

n = int(input("enter any number:"))

def calc_fact(n):
    ans=1

    for i in range(1,n+1):
        ans*=i
    return ans

print("factorial of ",n,"is : ",calc_fact(n))