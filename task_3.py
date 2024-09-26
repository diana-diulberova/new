# 5)Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность
# сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте
# отрицательных значений.

# 6) Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения

# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class Rectangle:
    """The Rectangle training class."""

    def __init__(self, *args):
        """Added length and width parameters."""
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width, _ = args

    def get_perimeter(self):
        """Method that returns the perimeter of the rectangle."""
        return self.length * 2 + self.width * 2

    def get_area(self):
        """Method that returns the area of a rectangle."""
        return self.length * self.width

    def __add__(self, other):
        """Method of adding two rectangles."""
        p = self.get_perimeter() + other.get_perimeter()
        return Rectangle(p // 2 / 2)

    def __sub__(self, other):
        """Method of subtracting two rectangles."""
        p = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(p // 2 / 2)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __str__(self):
        """Class representation for the print method."""
        return f'Прямоугольник со сторонами {self.length} и {self.width}'


rec_1 = Rectangle(5)
rec_2 = Rectangle(4)
print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
rec_3 = rec_1 + rec_2
rec_4 = rec_1 - rec_2
print(f'{rec_3.length = }\n{rec_3.width = }')
print(f'{rec_4.length = }\n{rec_4.width = }')
print(rec_1 == rec_2)
print(rec_3 <= rec_4)
help(Rectangle)
print(rec_1)
print(rec_3)
