print("Welcome to calculate your BMI : ")

# Please Input your height on Meter
your_height = input('Please Enter your Height on meter: \n')
# Please Enter your weight on kg
your_weight = input('Please Enter your weight on kg : \n')

# first you need to change data type str to flot or int
BMI_cal_1 = float(your_height)
BMI_cal_2 = int(your_weight)

BMI = BMI_cal_2 / (BMI_cal_1 * BMI_cal_1) # This is main math..

print('Your BMI weight is = ', + BMI)

if BMI < 15.0:
    print('You are Very severely UnderWeight ')
elif BMI <= 16.0:
    print('You are severely UnderWeight ')
elif BMI < 18.0:
    print('You are UnderWeight ')
elif BMI < 25.0:
    print('You are Normal(Healthy Weight) ')
elif BMI < 30.0:
    print('You are OverWeight ')
elif BMI < 35.0:
    print('You are Moderately Obese')
elif BMI < 40.0:
    print('You are Severely Obese')
elif BMI >= 40.0:
    print('You are very Severely Obese')
else:
    print('You are Wrong ')

