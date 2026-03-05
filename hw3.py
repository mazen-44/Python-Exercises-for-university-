def calc(g1,g2,g3):
    average = (g1+g2+g3) / 3
    return average
grades = []
for i in range(3):
    grade= float(input(f"Enter the grade {i+1} : "))
    grades.append(grade)
avg = calc(grades[0],grades[1],grades[2])
print(f"Your average is : {avg:.2f}")
