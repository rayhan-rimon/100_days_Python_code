print('Welcome to the love Calculator!')
name_1 = input('Please Enter your name: \n')
name_2 = input('Please Enter her name: \n')

# Calculation start
combined_str = name_1 + name_2
lower_case_str = combined_str.lower()


t = lower_case_str.count('t')
r = lower_case_str.count('r')
u = lower_case_str.count('u')
e = lower_case_str.count('e')

true = t + r + u + e

l = lower_case_str.count('l')
o = lower_case_str.count('o')
v = lower_case_str.count('v')
e = lower_case_str.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f'You love score is {love_score}, you go together coke and mentors')

elif (love_score >= 40) and (love_score <= 50):
    print(f'Your love score is {love_score}, you are alright together')
else:
    print(f'Your love score is {love_score}', )

