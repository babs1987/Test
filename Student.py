class Student:
    name = "Ivan"
    groupNumber = "10A"
    age = 18
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