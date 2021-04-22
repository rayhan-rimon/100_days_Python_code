# How to define a high score without using max() function

# input some list of score. as like 55 60 100 95 ...
student_scores = input('Input a list of students score: \n').split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print("List of student scores: ", student_scores)

height_score = 0
for score in student_scores:
    if score > height_score:
        height_score = score
print("The heights score in the class is : {a}".format(a = height_score))

