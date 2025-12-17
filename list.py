#list (mutable sequence of values)

marks = [99,89,100,65,92,"sravan"]
print(marks)

marks[2] = 70

print(marks)
print(type(marks))

#slicing

print(marks[4:6])

print(marks[-5:-2])

#list methods
nums = [1,2,3]
#append
nums.append(4)
#insert element with index
nums.insert(2,10)
print(nums)

#sort
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

#reverse
nums.reverse()
print(nums)