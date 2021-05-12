#This program make a simple Calculator

#define a function
def add(x, y):
    """This function Add Two numbers """
    return x + y

def subtract(x, y):
    """This function Subtracts Two numbers """
    return x - y

def multiply(x, y):
    """This function Multiply Two numbers """
    return x * y

def divide(x, y):
    """This function Divide Two numbers """
    return x / y

print('1. Sellect Operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

chose = input('Chose ane one above them 1/2/3/4 : ')

num_1 = int(input('Enter your first number: \n'))
num_2 = int(input('Enter your second number: \n'))

if chose == "1":
    print(num_1, "+", num_2, '=', add(num_1, num_2))

elif chose == "2":
    print(num_1, "-", num_2, '=', subtract(num_1, num_2))

elif chose == "3":
    print(num_1, "*", num_2, '=', multiply(num_1, num_2))

elif chose == "4":
    print(num_1, "/", num_2, '=', divide(num_1, num_2))

else:
    print("Invalid number!")
    print("I hop you chose invalid Operation. Please chose wright Operation")