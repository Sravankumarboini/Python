try:
    x = int(input("enter x value :"))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by zero is not allowed")

except ValueError:
    print("Invalid input")

else:
    print(f"ans = {ans}")

finally:
    print("end of program")