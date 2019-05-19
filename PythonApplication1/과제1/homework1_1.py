import person as p
if __name__=="__main__":
    peoples=[]
    names=["을지문덕","계백", "김유신", "강감찬", "이순신"]
    
    for i in range(5):
        name=names[i]
        age=int(input(names[i]+'의 나이: '))
        wei=int(input('몸무게: '))
        hei=int(input('키: '))
        var=p.person(name,i,age,hei,wei)
        peoples.append(var)


var=sorted(peoples,key=lambda person:person.age)
print("나이순")
for i in range(len(var)):
    print(var[i])

var=sorted(peoples,key=lambda person:person.height)
print("키순")
for i in range(len(var)):
    print(var[i])

var=sorted(peoples,key=lambda person:person.weight)
print("몸무게순")
for i in range(len(var)):
    print(var[i])
