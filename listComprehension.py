sq = [i*i for i in range(6)]

print(sq)

sqr = [i*i for i in range(10) if i%2!=0]

print(sqr)

nums = [-1,-1,2,3,4,-4]

nums = [0 if val<0 else val for val in nums]
print(nums)