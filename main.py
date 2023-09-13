#
print("Welcome to the tip calculator")
tot=float(input("what was the total bill? : $"))
per=float(input("What percentage tip would you like to give? 10, 12, 0r 15?  "))
split=int(input("How many people to split the bill?  "))
each=(tot/split)*(1+per/100)
pay=round(each,2)
print(f"each person should pay: ${pay} ")