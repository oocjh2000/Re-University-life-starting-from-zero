import School
import pickle
names=['유광무1','유광무2','유광무3','유광무4','유광무5']
kor=[23,45,34,76,98]
math=[23,45,34,76,98]
python=[23,45,34,76,98]
students=[]

for i in range(5):
    var= School.Student(names[i],i,kor[i],math[i],python[i])
    students.append(var)
f=open('나는_오이가_싫어요\data.bin','wb')
pickle.dump(students,f)
print('나는 오이가 싫어요')
