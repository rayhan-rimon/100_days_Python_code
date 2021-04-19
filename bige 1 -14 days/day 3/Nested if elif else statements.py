print('Welcome to the Roller Coaster!')
height = int(input('What is is you height in cm? \n'))

#Condition Start
if height >= 120:
    print('You can Ride the Roller Coaster!')

    # is if statement are true then Nested lis are enable
    age = int(input("What is your age? : "))
    if age < 12:
        print('Please pay $5 ')
    elif age <= 18:
        print('Please pay $7 ')
    else:
        print('Please pay $12 ')
else:
    print('You have to grow taller before you can Ride')