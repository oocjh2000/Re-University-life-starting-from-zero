import School
names = ['유광무1','유광무2','유광무3','유광무4','유광무5']
kor = [23,45,34,76,98]
math = [23,45,34,76,98]
python = [23,45,34,76,98]
students = []

for i in range(5):
    var = School.Student(names[i],i,kor[i],math[i],python[i])
    students.append(var)

sum = 0
for i in range(5):
    sum+=students[i].classes['python' + str(students[i].id)]
avr = sum // 5
print("파이썬 평균 :",avr)
for i in range(5):
    if students[i].classes['python' + str(students[i].id)] > avr:
        print(students[i].name)
