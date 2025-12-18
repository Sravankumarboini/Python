class student :
    def __init__(self,name,cgpa) :
        self.name = name
        self.cgpa = cgpa


stu1 = student("sravan kumar",8.5)
stu2 = student("sandeep",7.5)
stu3 = student("sathish",7.5)

print(stu1.name,stu1.cgpa)
print(stu2.name,stu2.cgpa)
print(stu3.name,stu3.cgpa)