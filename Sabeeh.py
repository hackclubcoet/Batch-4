student_height = input('Input a list of students: ').split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total = 0
number = 0
for heights in student_height:
    total += heights
    number += 1

avg = round(total / number)
print(f'The average height is {avg}')