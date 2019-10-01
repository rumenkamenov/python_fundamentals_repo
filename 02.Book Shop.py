
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) < 3:
            raise Exception("Title not valid!")
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if author.split()[1][0] in "0123456789":  # this will give the first letter of the author's last name
            raise Exception("Author not valid!")
        else:
            self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price is not valid!")
        else:
            self.__price = price

    def __str__(self):
        return f'Type: Book\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}\n'


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)
        self.__golden_price

    @property
    def golden_price(self):
        return self.__golden_price

    @golden_price.setter
    def price(self, price):
        if price < 0:
            raise Exception("Price is not valid!")
        else:
            self.__golden_price = price * 1.3

    def __str__(self):
        return f'Type: GoldenEditionBook\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.golden_price:.2f}\n'


author = input()
title = input()
price = float(input())

try:
    book = Book(title, author, price)
    print(book)
    golden_book = GoldenEditionBook(title, author, price)
    print(golden_book)
except Exception as exe:
    print(exe)

