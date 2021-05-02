print('Welcome to Python Pizza Deliveries!')

# Small Pizza : $15
# Medium Pizza : $20
# Large Pizza : $25
size = input('What size do you want? S, M, or L : ')

# Pepperoni for Small Pizza : + $2
# Pepperoni for Medium & Large Pizza : + $3
add_pepperoni = input('Do you want pepperoni? Y or N : ')

# Extra Cheese for any size Pizza : + $1
extra_cheese = input('Do you want extra cheese? Y or N : ')

# Main variable
bill = 0

# Conditional Statements Starts
if size =='s':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'y':
    bill += 1
# Conditional Statements End..

print(f'Your final bill is $ {bill}')
