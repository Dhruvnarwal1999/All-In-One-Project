# All in One Project Using by Def Function
import math
import random
print("<---------- Welcome To My Project ---------->")
ans='y'
print("\n<---------- PLEASE SELECT YOUR CHOICE ---------->")
print("\n1. Head and Tale Game Function Name Is Head() \n2. Calculator Funciton Name is Calculator() \n3. Quiz Game Function is Quiz() \n4. Clock Function is Clock() \n5. Shop Function is Shop()")
choice=input("\nChoice= ")
if choice=='1':
    a1=input("Define the Function= ")
    if a1=="Head()" or a1=="head()" or a1=="HEAD()":
        while ans=='y' or ans=='Y':
            def Head():
                h=0
                t=0
                q1=1
                while q1<=20:
                    a=random.random()
                    c=a*2
                    d=int(c)
                    if d==1:
                        h=h+1
                    else:
                        t=t+1
                    q1=q1+1
                    if h>t:
                        print("Winner is Head",h)
                    elif t>h:
                        print("Winner is tale",t)
                    elif t==h:
                        print("Match Tie")
                    ans=input("Would you like to play it again y/n..")
                    if ans!='y':
                        print("Thanks for playing this game I hope you like it")
                        break
            Head()
            break

if choice=='2':
    a=input("Enter the Function= ")
    if a=="Calculator()" or a=="calculator()" or a=="CALCULATOR()":
        while ans=='y':
            def Calculator():
                sum=0
                sub=0
                mul=1
                div=0
                area=0
                ans='y'
                choice=input("1. for Sum \t2. for Sub \n3. for Mul \t4. for Div \n5. For Power \t6. for Table= ")
                while ans=='y':
                    if choice=='1':
                        a=eval(input("Enter the value= "))
                        if a<0:
                            print("You are putting the wrong value= ",a)
                            break
                        else:
                            sum=sum+a
                        ans=input("Would you like to add more value y/n..= ")
                    if choice=='2':
                        a=eval(input("Enter the value= "))
                        if a<=0:
                            print("You are putting the wrong value= ",a)
                            break
                        if sub==0:
                            sub=a
                        else:
                            sub=sub-a
                            ans=input("Would you like to try it again y/n..= ")
                    if choice=='3':
                        a=eval(input("Enter the value= "))
                        if a<0:
                            print("You are putting the wrong value= ",a)
                            break
                        else:
                            mul=mul*a
                            ans=input("Would you like to add more value y/n..= ")
                    if choice=='4':
                        a=eval(input("Enter the First value= "))
                        b=eval(input("Enter teh Second value= "))
                        if a<0:
                            print("You are putting the wrong value= ",a)
                            break
                        else:
                            c=a/b
                            div=div+c
                            ans=input("Would you like to add more value y/n..= ")
                    if choice=='5':
                        a=eval(input("Enter the value= "))
                        if a<=0:
                            print("You are putting the wrong value= ",a)
                            break
                        else:
                            c=a**2
                            print(c)
                            ans=input("Would you like to add more value y/n..= ")
                    if choice=='6':
                        a=int(input("Enter the value= "))
                        for i in range(1,11):
                            b=a*i
                            print(a,'x',i,'=',b)
                        ans=input("Would you like to try again y/n..= ")
                    
                while choice=='1':
                    print("The Sum of the Total Values are= ",sum)
                    break
                while choice=='2':
                    print("The Sub of the Total Values are= ",sub)
                    break 
                while choice=='3':
                    print("The Mum of the Total Values are= ",mul)
                    break
                while choice=='4':
                    print("The sum of the Total Values are= ",sum)
                    break
            Calculator()
            break
if choice=='3':
    a=input("Enter teh Function= ")
    if a=="Quiz()" or a=="quiz()" or a=="QUIZ()":
        while ans=='y':
            def Quiz():
                #team
                team1=0
                team2=0
                #chances
                chance1=3
                chance2=3
                print("\nTeam1")
                q1="Q1= How many days are there in a week? \n1 = One \t2 = Three \n3 = Five \t4 = Seven"
                print(q1)
                choice=input("Answer= ")
                for i in range(chance1):
                    if choice=="4":
                        print("You are Correct")
                        team1=team1+1
                        break
                    else:
                        print("You are Wrong")
                        chance1=chance1-1
                        break
                print("\nTeam2")
                q2="\Q2= How many dare are there in a year? \n1 = 200 \t2 = 365 \n3 = 300 \t4 = 360"
                print(q2)
                choice=input("Answer= ")
                for i in range(chance2):
                    if choice=="2":
                        print("You are Correct")
                        team2=team2+1
                        break
                    else:
                        print("You are Wrong")
                        chance2=chance2-1
                        break
                print("\nTeam1")
                q3="\nQ3= Which animal is known as the 'Ship of the Desert?' \n1 = Tiger \t2 = Lion \n3 = Elephant \t4 = Camel"
                print(q3)
                choice=input("Answer= ")
                for i in range(chance1):
                    if choice=="4":
                        print("You are Correct")
                        team1=team1+1
                        break
                    else:
                        print("You are Wrong")
                        chance1=chance1-1
                        break
                print("\nTeam2")
                q4="\nQ4= How many letter are there in English alphabet? \n1 = 20 \t2 = 26 \n3 = 23 \t4 = 15"
                print(q4)
                choice=input("Answer= ")
                for i in range(chance2):
                    if choice=="2":
                        print("You are Correct")
                        team2=team2+1
                        break
                    else:
                        print("You are Wrong")
                        chance2=chance2-1
                        break
                print("\nTeam 1")
                q5="\nQ5= In which direction does the Sunrise? \n1 = East \t2 = West \n3 = North \t4 = South"
                print(q5)
                choice=input("Answer= ")
                for i in range(chance1):
                    if choice=="1":
                        print("You are Correct")
                        team1=team1+1
                        break
                    else:
                        print("You are Wrong")
                        chance1=chance1-1
                        break
                print("\nTeam 2")
                q6="\nQ6= How many sides are there in a triangle? \n1 = One \t2 = Two \n3 = Three \t4 = Four"
                print(q6)
                choice=input("Answer= ")
                for i in range(chance2):
                    if choice=='3':
                        print("You are Correct")
                        team=team2+1
                        break
                    else:
                        print("You are Wrong")
                        chance2=chance2-1
                        break
                print("\nTeam1")
                q7="\nQ7= Which month of the year has the least number of days? \n1 = January \t2 = February \n3 = March \t4 = April"
                print(q7)
                choice=input("Answer= ")
                for i in range(chance1):
                    if choice=='2':
                        print("You are Correct")
                        team1=team1+1
                        break
                    else:
                        print("You are Wrong")
                        chance1=chance1=1
                        break
                print("\nTeam 2")
                q8="\nQ8= Which animal is called King of Jungle? \n1 = Lion \t2 = Tiger \n3 = Elephant \t4 = Monkey"
                print(q8)
                choice=input("Answer= ")
                for i in range(chance2):
                    if choice=="1":
                        print("You are Correct")
                        team2=team2+1
                        break
                    else:
                        print("You are Wrong")
                        chance2=chance2-1
                        break
                print("\nTeam 1")
                q9="\nQ9= How many days are there in the month of February in a leap year? \n1 = 28 \t2= 29 \m3 = 30 \t4 = 31"
                print(q9)
                choice=input("Answer= ")
                for i in range(chance1):
                    if choice=='2':
                        print("You are Correct= ")
                        team1=team1+1
                        break
                    else:
                        print("You are Wrong")
                        chance1=chance1-1
                        break
                print("\nTeam 2")
                q10="\nQ10= What is the top color in a rainbow? \n1 = Red \t2 = White \n3 = Blue \t4 = Pink"
                print(q10)
                choice=input("Answer= ")
                for i in range(chance2):
                    if choice=="1":
                        print("You are Correct")
                        team2=team2+1
                        break
                    else:
                        print("You are Wrong")
                        chance2=chance2-1
                        break
                while team1>team2:
                    print("Team 1 is Winner")
                    print("Team 2 better luck for next time")
                    break
                while team1==team2:
                    print("Match Tie")
                    print("Both team are doing good")
                    break
                while team2>team1:
                    print("Team 2 is Winner")
                    print("Team 1 Better luck for next time")
                    break
            Quiz()
            break
if choice=='4':
    a=input("Enter the Function= ")
    if a=='Clock()' or a=='clock()' or a=='CLOCK()':
        while ans=='y':
            def Clock():
                i=1
                while i<=24:
                    j=0
                    while j<=59:
                        if j<12:
                            print(i,":",j,"AM")
                        else:
                            print(i,":",j,"PM")
                        j=j+1
                    i=i+1
            Clock()
            break

if choice=='5':
    a=input("Enter the Function= ")
    if a=='shop()' or a=='Shop()' or a=='SHOP()':
        def shop():
            # This is a project for shop
            l1=[] # This for Amount
            l2=[] # This for Items
            l3=[] # This for price
            while True:
                print("1. Veg")
                print("2. Non-Veg")
                print("3. Sweets")
                print("4. Exit")
                choice=int(input("Enter your choice= "))
                if choice==1:
                    q1=["Burger","Pizza","Dosa","Noodle"]
                    choice=int(input("Enter your choice \n1. for Burger Rs. 50/- \t2. for Pizza Rs. 100/- \n3. for Dosa Rs. 150/- \t4. for Noodle 80/-"))
                    if choice==1:
                        a=int(input("Enter the Quantity= "))
                        b=50*a
                        l1.append(a)
                        l2.append(q1[0])
                        l3.append(b)
                    elif choice==2:
                        a=int(input("Enter the Quantity= "))
                        b=100*a
                        l1.append(a)
                        l2.append(q1[1])
                        l3.append(b)
                    elif choice==3:
                        a=int(input("Enter the Quantity= "))
                        b=150*a
                        l1.append(a)
                        l2.append(q1[2])
                        l3.append(b)
                    elif choice==4:
                        a=int(input("Enter the Quantity= "))
                        b=80*a
                        l1.append(a)
                        l2.append(q1[3])
                        l3.append(b)
                    else:
                        print("You are Selected the Wrong Number. Please Try Again")
                elif choice==2:
                    q2=["Chicken","Omlet"]
                    print(q2)
                    choice=int(input("Enter Your Choice \n1. for Chicken Rs. 250/- \t2. for Omlet Rs. 70/- = "))
                    if choice==1:
                        l2.append(q2[0])
                        q3=["Normal Chicken","Grilled Chicken"]
                        print(q3)
                        choice=int(input("Enter your Choice 1 or 2 = "))
                    elif choice==1:
                        a=int(input("Enter the Quantity= "))
                        b=250*a
                        l1.append(a)
                        l2.append(q3[0])
                        l3.append(b)
                    elif choice==2:
                        l2.append(q2[1])
                        a=int(input("Enter the Quantity= "))
                        b=250*a
                        l1.append(a)
                        l2.append(q3[1])
                        l3.append(b)
                    else:
                        print("You are selected the wrong Number. Please try Again")
                elif choice==3:
                    q4=["Cold Coffee","Coffee","Pepsi","Water Bottle"]
                    choice=int(input("Enter your choice \n1. Cold Coffee Rs. 50/- \t2. Coffee Rs. 30/- \n3. Pepsi Rs. 20/- \t4. Water Bottle Rs. 10/-"))
                    if choice==1:
                        a=int(input("Enter the Quantity= "))
                        b=6*a
                        l1.append(a)
                        l2.append(q1[0])
                        l3.append(b)
                    elif choice==2:
                        a=int(input("Enter the Quantity= "))
                        b=30*a
                        l1.append(a)
                        l2.append(q1[1])
                        l3.append(b)
                    elif choice==3:
                        a=int(input("Enter the Quantity= "))
                        b=20*a
                        l1.append(a)
                        l2.append(q1[2])
                        l3.append(b)
                    elif choice==4:
                        a=int(input("Enter the Quantity= "))
                        b=10*a
                        l1.append(a)
                        l2.append(q1[3])
                        l3.append(b)
                    else:
                        print("You are slected the Wrong Number. Please try Again")
                else:
                    total1=sum(l1)
                    total2=sum(l3)
                    print("You are Selected",total1,"Items",l2,"and the amount is",total2)
                    print("You will get your order Soon\nThanks for Coming. Hope you like the service")
                    break
        shop()
