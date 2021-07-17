# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights : ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

#! The rules is you cannot use len() and sum() functions.

a = 0
b = 0
for x in student_heights:
    a += x
    b += 1

print(round(a / b))
