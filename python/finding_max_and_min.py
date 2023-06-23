student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

n = student_scores[0]

for i in student_scores:
    if i > n:
        n = i

print (f"The highest score in the class is: {n}")

nl = student_scores[0]

for i in student_scores:
    if i < nl:
        nl = i

print (f"The lowest score is {nl}")
