student_grades = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 70, 65, 89]

print(sum((student_grades)))
print(max((student_grades)))

sum = 0
highest = 0
for grade in student_grades:
    sum += grade
    if highest < grade:
        highest = grade


print(sum)
print(highest)