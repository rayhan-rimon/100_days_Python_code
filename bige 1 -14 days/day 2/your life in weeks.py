# whrite your age age know how maney week, day you live in

age = input('What is your current age? \n')
# age conver str to int
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaininig = years_remaining * 12

print(f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaininig} months left.')


