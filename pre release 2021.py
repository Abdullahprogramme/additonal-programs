Highest= 0
Choice="YES"
Train=["09:00" ,"11:00" ,"13:00" ,"15:00" ,"10:00" ,"12:00" ,"14:00" ,"16:00"]
Passangers=[0,0,0,0,0,0,0,0]
Seats=[480,480,480,480,480,480,480,640]
Cost=[0,0,0,0,0,0,0,0]
for Count in range(7):
    print(str(Train[Count]) + "            " + str(Seats[Count]) + "              " + str(Cost[Count]) + "$")
while Choice == "YES" : 
    print("How many tickets do you want")
    Tickets=input()
    print("In which train do you want to travel upwards")
    DepartureTrain=input()
    print("In which train do you want to travel downwards")
    ArrivalTrain=input()
    if DepartureTrain== "09:00" or "11:00" or "13:00" or "15:00":
        for Count in range(3):
            if DepartureTrain==Train[Count]:
                Temp1=Count
        while Tickets > Seats[Temp1]:
            if Tickets > Seats[Temp1]:
                print("Wrong tickets entered, re-enter")
                Tickets=input()    
        Seats[Temp1]=Seats[Temp1]-Tickets
        Passangers[Temp1]=Passangers[Temp1]+ Tickets
        if Tickets >=10 and Tickets >80 :
             FreeTickets=int(Tickets/10)
        Cost[Temp1]=Cost[Temp1] + 25 * (Tickets-FreeTickets)
    if ArrivalTrain== "10:00" or "12:00" or "14:00" or "16:00" :
        for Count in range(4,7):
            if ArrivalTrain==Train[Count]:
                Temp2=Count   
        Seats[Temp2]=Seats[Temp2]-Tickets
        Passangers[Temp2]=Passangers[Temp2]+ Tickets
        if Tickets >=10 and Tickets >80 :
             FreeTickets=int(Tickets/10)
        Cost[Temp2]=Cost[Temp2] + 25 * (Tickets-FreeTickets)    
    for Count in range(7):
        if Seats[Count]=="0" :
            Seats[Count]="Closed"
    for Count in range(7):
        print(str(Train[Count]) + "            " + str(Seats[Count]) + "              " + str(Cost[Count]) + "$")
    print("Do you want to buy more tickets ")
    Choice=input()
for Count in range(7) :
    TotalMoney = TotalMoney + Cost[Count]
    TotalPassangers = TotalPassangers + Passangers[Count]
    if Passangers[Count] > Highest :
        Highest = Passangers[Count]
        MostPassangers = Count
print("The most passanger train was " + Train[MostPassangers])
print("The total money was " + str(TotalMoney))
print("The total passangers were " + str(TotalPassangers))