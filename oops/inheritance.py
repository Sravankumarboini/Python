#inheritance (reusing attributes and methods from parent class)

class employee:
    start_time = "10am"
    end_time = "4pm"


class teacher(employee):

    def __init__(self, subject):
        self.subject = subject
    
t1 = teacher("Math")

print(t1.subject,t1.start_time,t1.end_time)