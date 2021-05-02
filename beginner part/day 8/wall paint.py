# Wall painting exercise
# How many cage need to a wall pain
# Each cage able to pain 5 square wall

# start programming
import math
def paint_cal(height, width, cover):
    area = height * width
    num_can = math.ceil(area / cover)
    print("You will need {a} can of paints".format(a=num_can))



t_height = int(input("Enter your wall height: "))
t_width = int(input("Enter your wall width: "))
coverage = 5
paint_cal(height=t_height, width=t_width, cover=coverage)