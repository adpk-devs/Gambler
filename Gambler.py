#Slot machine
print("Welcome to the slot machine.")

import pandas as pd
import numpy as np
import os 
import time
import random


slot=[]
error=0
points=int(0)
while True:
    if error==0:
        if points>0:
            opt=int(input('''If you want to add money, enter '1'.
If you want to continue gambling, enter '0'.
'''))
        elif error==0:
            opt=1
        elif error==1:
            opt=1
        elif error==2:
            opt=0
    if opt==1:
        if error==0:
            money=int(input("How much money do you want to add?(Max 100$):"))
        elif error==1:
            money=int(input("Enter a valid amount!:"))
            error=0
        else:
            pass
    else:
        pass
    if money<=100:
        pass
    else:
        print("\nYou can't add that much money!\n")
        error=1
        continue
    if opt==1:
        points+=money
 
    print('\n\nYour current money:',points,"$")

    if error==2:
        pt=int(input('Enter an amount in accordance to your status(Wallet):'))
    else:
        pt=int(input('How much money would you like to bet?:'))
    
    if pt<=points:
        pass
    else:
        print("\nYou don't have that much money!\n")
        error=2
        continue
    
    for i in range(0,25):
        slot=[]
        val=np.random.randint(1,4,size=3)
        for i in range(len(val)):
        
            if val[i]==1:
                slot.append('♦')
            elif val[i]==2:
                slot.append('♥')
            else:
                slot.append('♠')
        dia=[]
        heart=[]
        ace=[]
    

        for i in range(len(val)):
            if slot[i]=='♦':
                 dia.append(slot[i])
            elif slot[i]=='♥':
                 heart.append(slot[i])
            elif slot[i]=='♠':
                 ace.append(slot[i])
        print('''Welcome to the slot machine.


Your current money:''',points,"$")
        print("How much money would you like to bet?:",pt,"\n")
        print("               ",slot[0],"   ",slot[1],"   ",slot[2])  
        
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")

        
        
    print('''Welcome to the slot machine.


Your current money:''',points,"$")
    print("How much points would you like to bet?:",pt,"\n")    
    print("               ",slot[0],"   ",slot[1],"   ",slot[2])
        
        
    print("\n\nResult:",slot)
    if len(dia)==3 or len(heart)==3 or len(ace)==3:
        print("Jackpot!")
        print(pt*7,'$ added to your wallet!')
        points+=pt*7
        
    elif len(dia)==2 or len(heart)==2 or len(ace)==2:
        print("You broke even.")
        points=points-(pt*0.5)
        
    else:
        print("You lost!, better luck next time.")
        points=points-pt
        
    print('\n\nYour current money:',points,"$")


