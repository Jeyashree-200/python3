s1=input("enter the 1st string:")
s2=input("enter the 2nd string:")
if len(s1)==len(s2) and s2 in (s1+s1):
    print("the strings are rotated")
else:
    print("the strings are not rotated")
