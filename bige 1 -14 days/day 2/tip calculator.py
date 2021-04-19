print("Welcome to the tip Calculator.")
bill = input("What was the total bill? \n$")
# Bill convert str to int
bill_as_int = int(bill)

tips = input('What percentage tip would you like to give? 10, 12, or 15? \n')
# tips convert str tp int
tips_as_int = int(tips)

person = input('How many people to split the bill? \n')
# person convert str to int
person_as_int = int(person)

# bill with tips calculate >> how much to pay with them..
bill_with_tips = ((tips_as_int / 100) * bill_as_int) + bill_as_int

# each person should be pay ...How much ? $
each_person_should_be_pay = round(bill_with_tips / person_as_int, 2)

print(f'Each person should pay : \n${each_person_should_be_pay}')


