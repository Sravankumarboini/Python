dict = {}

while True:
    print("Menu:")
    print("A - add a student ")
    print("B - update marks ")
    print("c - search for a student ")
    print("D - display all students ")
    print("E - Exit ")

    choice = input("enter your choice ")

    if choice == 'A':
        name =  input("enter the name : ")
        marks = int(input("enter marks :"))
        dict[name] = marks
    elif choice == 'B':
        name =  input("enter the name : ")
        marks = int(input("enter marks :"))
        dict[name] = marks
    elif choice == 'C':
        name = input("enter the name")
        print(f"{name} marks = {dict[name]}")
    elif choice == 'D':
        for name,marks in dict.items():
            print(name , ":",marks)
    elif choice == 'E':
        break
