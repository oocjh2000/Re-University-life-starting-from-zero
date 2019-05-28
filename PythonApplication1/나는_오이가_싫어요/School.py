class Person(object):
     def __init__(self,name,id):
        self.name=name
        self.id=id
   

class Student(Person):
    def __init__(self, name, id,kor,math,python):
         super().__init__(name, id)
         self.classes={}
         self.classes['kor'+str(id)]=kor
         self.classes['math'+str(id)]=math
         self.classes['python'+str(id)]=python

    def GetGPA(self):
        return (self.classes['kor'+str(id)]+self.classes['math'+str(id)]+self.classes['python'+str(id)])/3


