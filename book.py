class Book:
    def __init__(self, title, fio, year, genre, pages):
        self.title = title
        self.fio = fio
        self._year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return f"назв: {self.title} фио: {self.fio} год: {self.year} Жанр: {self.genre} кол.стр: {self.pages}"

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year


b1 = Book("some", "vasia pupkin", 1666, "genre", 888)
print(b1)
print(b1.year)
b1.year=1999
print(b1)
