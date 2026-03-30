s=input("enter the sentence")
word=s.split()
for w in word:
    if len(w)>5:
        print(w)
