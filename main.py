students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
name_students = list(students)
n1 = sorted(name_students)
s1 = sum(grades[0]) / len(grades[0])
s2 = sum(grades[1]) / len(grades[1])
s3 = sum(grades[2]) / len(grades[2])
s4 = sum(grades[3]) / len(grades[3])
s5 = sum(grades[4]) / len(grades[4])
a = {n1[0]: s1}
b = {n1[1]: s2}
c = {n1[2]: s3}
d = {n1[3]: s4}
e = {n1[4]: s5}
student_average = {}
student_average.update(a)
student_average.update(b)
student_average.update(c)
student_average.update(d)
student_average.update(e)
print(student_average)