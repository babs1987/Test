class Country:
    def __init__(self,population=0):
        self.population=population

    def set_population(self,pop):
        self.population=pop

    def get_population(self):
        return self.population
    
    
class Russia(Country):
    def __init__(self,population=144100000):
        super().__init__(population)

class Canada(Country):
    def __init__(self,population=38000000):
        super().__init__(population)
class Germany(Country):
    def __init__(self, population=83000000):
        super().__init__(population)

r=Russia()
print(r.get_population())
s=Germany()
print(s.get_population())

