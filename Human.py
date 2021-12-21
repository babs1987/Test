class Human:
    def __init__(self, fio="no", age="no", phone="no", city="no", country="no", address="no"):
        self.fio = fio
        self.age = age
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def about(self):
        return "abstract human"

    def what_i_do(self):
        return "some"


class Student(Human):
    def about(self):
        return f"Студент: ФИО: {self.fio}, Дата рождения:{self.age},телефон {self.phone}, город:{self.city}, страна:{self.country}, адрес: {self.address}"

    def what_i_do(self):
        return "Studying..."


class Worker(Human):
    def about(self):
        return f"Работяга: ФИО: {self.fio}, Дата рождения:{self.age},телефон {self.phone}, город:{self.city}, страна:{self.country}, адрес: {self.address}"

    def what_i_do(self):
        return "Working..."

some = Human()
print(some.about(), some.what_i_do())
oleg = Student("Хулиганов Олег Петрович", "10.10.1998", "+78737237423", "New Kuznetsk", "Russian Federation",
               "Pushkina Kolotushkina")
print(oleg.about(), oleg.what_i_do())

volodia = Worker("Уличный Володя Петрович", "10.10.1978", "+78745637423", "New Chara", "Russian Federation",
               "34 Alexa Kurdechi 123")

print(volodia.about(),volodia.what_i_do())