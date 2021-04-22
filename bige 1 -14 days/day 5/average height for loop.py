# Define a average number without using sum() & len() function

# User Input some people height in cm.
student_height = input("Input a list of student's height: \n").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)
# For loop
total_height = 0
for height in student_height:
    total_height += height

print('Total Height: \n', total_height)

num_of_students = 0
for student in student_height:
    num_of_students += 1
print('Number of students: \n', num_of_students)

average_height = round(total_height / num_of_students)
print('Average Height: \n', average_height)