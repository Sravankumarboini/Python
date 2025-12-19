s = input()

flag=1

def check_palindrome(s):
    st = 0 
    end = len(s) - 1
    while st < end/2:
        if(s[st] != s[end]):
            return False
        st+=1
        end-=1
    return True

if(check_palindrome(s)):
    print("palindrome")
else:
    print("not palindrome")