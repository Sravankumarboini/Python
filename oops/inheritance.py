#inheritance (reusing attributes and methods from parent class)

class employee:
    start_time = "10am"
    end_time = "4pm"

class teacher(employee):#single inheritance

    def __init__(self, subject):
        self.subject = subject
    
t1 = teacher("Math")

print(t1.subject,t1.start_time,t1.end_time)


#multi inheritance

class AdminStaff(employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(25_000, "ca")

print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

#multiple inheritance

class teacher:
    def __init__(self, salary):
        self.salary = salary

class student(teacher):
    def __init__(self, gpa):
        self.gpa = gpa

class TA(teacher, student):
    def __init__(self, salary, gpa, name):
        super.__init__(salary)
        student.__init__(slef, gpa)
        self.name = name

   ta1 = TA(15000, 9.3, "sravan kumar")     