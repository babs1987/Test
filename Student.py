class Student:
    def __init__(self,name="Ivan",groupNumber="10a",age=18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self,name,age):
        self.name=name
        self.age=age
    def setGroupNumber(self,gn):
        self.groupNumber=gn


tol=Student()

print(tol.getName())