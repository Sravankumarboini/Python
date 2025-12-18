class student :
    def __init__(self,name,cgpa) :#self is reference to that particular object
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self) :
        return self.cgpa


stu1 = student("sravan kumar",8.5)
stu2 = student("sandeep",7.5)
stu3 = student("sathish",7.5)

print(stu1.name,stu1.cgpa)
print(stu2.name,stu2.cgpa)
print(stu3.name,stu3.cgpa)

print(stu1.get_cgpa())


class stu :
    college_name = "abc college" #class attribute

    def __init__(self, name, cgpa) :
        self.name = name #object atrribute(these changes according to object)
        self.cgpa = cgpa

st1 = stu("sravan kumar",8.5)

print(st1.college_name)
print(stu.college_name)
print(st1.name)
print(st1.cgpa)


class Laptop :
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    
    @classmethod #decorator
    def get_storage_type(cls):#class method
        print(f"storage_type = {cls.storage_type}")

    def get_info(self): #instance method
        print(f"laptop has {self.RAM} & {self.storage} {self.storage_type}")
l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()

l1.get_storage_type()