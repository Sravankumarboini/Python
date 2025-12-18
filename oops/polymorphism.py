#polymorphism (same name -> many forms)

class employee:
    def get_designation(self):
        print("designation = employee")

class teachear(employee): #funtion overrinding
    def get_designation(self):
        print("designation = teacher")

t1 = teachear()
t1.get_designation()

#duck typing(walking like a duck and quaks like a duck)

class student:
    def get_designation(self):
        print("designation = student")

class accountant:
    def get_designation(self):
        print("designation = accountant")

t2 = student()
t2.get_designation()

acc1 = accountant()
acc1.get_designation()
