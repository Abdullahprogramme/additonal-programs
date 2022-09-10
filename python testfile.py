Words={}
Line=input("Type a sentence: ")
Line = Line.split(" ")
for a in Line:
    Words[a] = Words.get(a,0) + 1
print(Words)
temp=list()
for k,v in Words.items():
    newt=(v,k)
    temp.append(newt)

print("Flipped",temp)