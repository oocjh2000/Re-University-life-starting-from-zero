import pickle
import School
f = open('나는_오이가_싫어요\data.bin','rb')
students = pickle.load(f)

sum = 0
for i in range(5):
    sum+=students[i].classes['python' + str(students[i].id)]
avr = sum // 5
print("파이썬 평균 :",avr)
for i in range(5):
    if students[i].classes['python' + str(students[i].id)] > avr:
        print(students[i].name)