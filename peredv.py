class Srper:
    pass
#масса машины в тоннах
class Car(Srper):
    def __init__(self,mass,tank):
        self.mass=mass
        self.tank=tank

    def drive(self,range):
        if range>self.tank/(self.mass/5*20)*100:
            return f"авто проехало {self.tank/(self.mass/5*20)*100} километров"
        else:
            return "порядок, приехали"

#масса повозки в тоннах
class Kon(Srper):
    def __init__(self,horses,mass):
        self.horses=horses
        self.mass=mass
    def drive(self,range):
        if range>(self.horses*100/self.mass):
            return f"повозка проехала {self.horses*100/self.mass} километров лошади сдохли"
        else:
            return "порядок, приехали"

bmw=Car(2,100)
Plotvaandplotvadva=Kon(2,2)
print(Plotvaandplotvadva.drive(500))
print(bmw.drive(5000))

