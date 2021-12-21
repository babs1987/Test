class Book:
    def __init__(self, title, fio, year, genre, pages):
        self.title = title
        self.fio = fio
        self.year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return f"назв: {self.title} фио: {self.fio} год: {self.year} Жанр: {self.genre} кол.стр: {self.pages}"

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year


b1 = Book("some", "vasia pupkin", 1666, "genre", 888)
print(b1)
print(b1.get_year())
