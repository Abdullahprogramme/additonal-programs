
def Add():
    user=input("Enter your username: ") 
    pwd=input("Enter your password: ") 
    with open("password.txt","a") as f:
        f.write(user + "/" + pwd + "\n")
    f.close()
def View():
    dict={}
    with open("password.txt","r") as f:
        achoice=input("Do you want to view all password or single: ")
        if achoice=="All":
            for line in f.readlines():
                line.rstrip()
                a,b=line.split("/")
                print("Usernaem is '" + a + " 'and password is '" + b +"'")
        elif achoice=="Single":
            for line in f.readlines():
                line.rstrip()
                a,b=line.split("/")
                dict[a]=b
            users=input("Enter the username you want to search: ")
            print(dict[users])
    f.close()
 

name=input("Enter your name: ")
while True:
    choice=input("Do you want to add , view the password or quit program " + name +" .('Add','View',''Quit')")
    if choice=="Quit":
        print("GoodBye")
        quit()
    if choice=="Add":
        Add()
    elif choice=="View":
        View()

