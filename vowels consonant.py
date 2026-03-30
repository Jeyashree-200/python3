s=input("enter string")
s=s.lower()
v=0
con=0
for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            v+=1
        else:
            con+=1
print("vowels:",v)
print("consonants:",con)
