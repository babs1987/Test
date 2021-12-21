class Srper:
    pass
#масса машины в тоннах
class Car(Srper):
    def __init__(self,mass,tank):
        self.mass=mass
        self.tank=tank

    def drive(self,range):
        rashod=self.mass/5*20
        actual=self.tank/rashod*100
        if range>actual:
            return f"авто проехало {actual} километров"
        else:
            return "порядок, приехали"

#масса повозки в тоннах
class Kon(Srper):
    def __init__(self,horses,mass):
        self.horses=horses
        self.mass=mass
    def drive(self,range):
        actual=self.horses*100/self.mass
        if range>actual:
            return f"повозка проехала {actual} километров лошади сдохли"
        else:
            return "порядок, приехали"

bmw=Car(2,100)
Plotvaandplotvadva=Kon(2,2)
print(Plotvaandplotvadva.drive(500))
print(bmw.drive(5000))
