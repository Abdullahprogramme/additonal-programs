print("Enter numbers")
Num=input()
#filename=input("Enter a file name: ")
#fh=open(filename)
DNum={}
Num.rstrip()
number=Num.split(" ")
for a in number:
    DNum[a]=DNum.get(a,0) + 1
print(DNum)