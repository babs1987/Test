class Country:
    population=0
    def set_population(self,pop):
        self.population=pop

    def get_population(self):
        return self.population
class Russia(Country):
    population = 144000000

class Canada(Country):
    population = 909

class Germany(Country):
    population = 11488

s=Germany()
print(s.get_population())

