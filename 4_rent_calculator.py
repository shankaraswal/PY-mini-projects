
rent_pm = int(input("Please enter this month FLAT RENT: "))
cook_pm = int(input("Please enter this moth COOK SALARY: "))
elect_pm = int(input("Please enter this month ELECTRICITY UNIT(S): "))
elect_pu = int(input("Please enter ELECTRICITY PER UNIT CHARGES: "))
grocery_pm = int(input("Please enter this month GROCERY BILL: "))

room_mates = int(input(f"Please enter how many ROOM MATE(s) with you: "))

total_elect = elect_pm * elect_pu


expnses_pm = rent_pm + cook_pm + grocery_pm + total_elect
total_flatmates = int(room_mates +1)

per_mate = expnses_pm // room_mates

print(f"\nYou and your room mate's should contribute ${per_mate} for this month".upper())












