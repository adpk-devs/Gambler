# Slot machine.
print("""                                               Welcome to the slot machine!""")

import os
import time

import numpy as np

money = 0
debt = 0
earnings = 0
result = "win"

while True:
    # Money Loaning
    while True:
        if money > 0:
            opt = input("Do you want to loan more money?('Yes' or 'No'):").lower()
            if opt == "yes" or opt == "no":
                break
            else:
                print("Please enter 'Yes' or 'No'!")
                continue
        else:
            opt = "yes"
        break

    while True:
        if opt == "yes":
            loan = int(input("\nHow much money would you like to loan?(Max 100$):"))
        else:
            loan = 0

        if loan > 100:
            print("\nYou can't loan that much money!")
            continue
        print(loan, "$  added to your wallet")
        print(loan, "$  added to your debt")
        break

    if opt == "yes":
        money += loan
        debt += loan
    print("\nWallet:", money, "$")
    print("Debt:", debt, "$")

    # Betting
    while True:
        bid = int(input("How much money would you like to bet?:"))
        print("\n")
        if bid <= money:
            break
        else:
            print("Enter an amount in accordance to your status(Wallet)!\n")
            continue

    # SlotMachine
    for i in range(25):
        slot = []
        val = np.random.randint(1, 4, size=3)
        for i in range(len(val)):
            if val[i] == 1:
                slot.append("♦")
            elif val[i] == 2:
                slot.append("♥")
            else:
                slot.append("♠")
        dia = []
        heart = []
        ace = []

        for i in range(len(val)):
            if slot[i] == "♦":
                dia.append(slot[i])
            elif slot[i] == "♥":
                heart.append(slot[i])
            elif slot[i] == "♠":
                ace.append(slot[i])

        print(
            "                                         ",
            slot[0],
            "     ",
            slot[1],
            "     ",
            slot[2],
        )
        time.sleep(0.1)
        print("\033[A                             \033[A")

    # Result determination
    print("\n\nResult:", slot)
    if len(dia) == 3 or len(heart) == 3 or len(ace) == 3:
        print("Three of a kind - Jackpot!")
        earnings = bid * 3
        if debt > 0:
            if earnings * 0.5 > debt:
                print(
                    earnings * 0.5 + (earnings * 0.5 - debt), "$ added to your wallet!"
                )
                print(debt, "$ Subtracted from your debt!")
                print("Debt Cleared!")
            else:
                print(earnings * 0.5, "$ added to your wallet!")
                print(earnings * 0.5, "$ Subtracted from your debt!")
        else:
            print(earnings, "$ added to your wallet!")
        result = "win"

    elif len(dia) == 2 or len(heart) == 2 or len(ace) == 2:
        print("Two of a kind - You get your bid back.")
        if debt > 0:
            print(round(debt * 0.1, 0), "$ added to your debt.")
            debt += round(debt * 0.1, 0)
        earnings = 0
        result = "draw"
    else:
        print("One of a kind - You lost!")
        print(bid, "$ deducted from your wallet")
        earnings = -bid
        result = "lose"

    print("\nEnter anything to continue:")
    input()
    os.system("cls" if os.name == "nt" else "clear")

    # Wallet calculation
    if debt > 0:
        if result == "win":
            if earnings * 0.5 > debt:
                money += (earnings * 0.5) + (earnings * 0.5 - debt)
                debt = 0
            else:
                debt -= earnings * 0.5
                money += earnings * 0.5
        else:
            money += earnings
    else:
        money += earnings

    if debt > 0:
        if result == "win":
            if earnings * 0.5 > debt:
                print(
                    "\n\nWallet:",
                    money,
                    "$",
                )
                print("Debt: None")
            else:
                print("\n\nWallet:", money, "$")
                print("Debt:", debt, "$")
        else:
            print("\n\nWallet:", money, "$")
            print("Debt:", debt, "$")
    else:
        print("\n\nWallet:", money, "$")
        print("Debt: None")
