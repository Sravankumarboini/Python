'''
age=int(input("Enter your age : "))

if(age>18) :
    print("You can vote")
else :
    print("You can't vote")
'''

#match case(like switch)

color = input("enter color: ")

match color:
    case "green":
        print("Go")
    case "yellow":
        print("look")
    case "red":
        print("stop")