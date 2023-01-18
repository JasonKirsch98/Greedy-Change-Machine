cont = True#Used to quit program
q = 10#Starting stock
d = 10
n = 10
p = 10
while cont:#Run until out of change or q inputted 
    cost = input("Enter purchase price (xx.xx) or 'q' to quit: ")#Prompt user for price
    print(cost)
    if cost == 'q':
        cont = False#If q is entered, program quit
    elif float(cost) < 0:#If input negative, start over
        print("Price must be positive")
    else:
        cost = float(cost)
        payment = int(input("Enter dollars paid: "))#Get payment
        while(payment < cost):#Guarentee payment greather than cost
            print("Insufficient payment")
            payment = int(input("Enter dollars paid: "))
        change = payment - cost
        change = round(change*100) #convert from dollars to pennies to eliminate float rounding errors
        numQ = int(change/25)#Calculates Quarters due
        if numQ > q:#If quarters insufficent
            numQ = q
        change = change - numQ*25#Calculates remaining change
        q = q-numQ#Remove quarters from register
        numD = int(change/10)
        if numD > d:#Calculates Dime due
            numD = d
        change = change - numD*10
        d = d-numD
        numN = int(change/5)
        if numN > n:#Calculates Nickles due
            numN = n
        change = change - numN*5
        n = n-numN
        numP = int(change)
        if numP > p:#Calculates Pennies due
            numP = p
        change = change-numP
        p = p-numP
        
        if(change > 0):#Outstanding change
            print("Error, out of coins")
            cont = False
        else:#Display result
            print("Change:")
            print("Quarters: " + str(numQ))
            print("Dimes: " + str(numD))
            print("Nickes:"+ str(numN))
            print("Pennies:"+ str(numP))
            
            print("Stock: " + str(q) + " quarters " + str(d) + " dimes " + str(n) + " nickles " + str(p) + " pennies")
            
# Questions
#Q1:7
#Q2:5
#Q3:3
#Q4:6
#Q5:1
