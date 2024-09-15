# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа. Внутри класса создайте экземпляр на основе переданного
# типа и верните его из класса-фабрики.

from task_5 import Birds, Fish, Mammals, Animals


class Fabric:
    def __init__(self, obj_class, *args, **kwargs):
        self.obj_class = obj_class
        if self.obj_class == Birds:
            self.object = Birds(*args, **kwargs)
        elif self.obj_class == Fish:
            self.object = Fish(*args, **kwargs)
        elif self.obj_class == Mammals:
            self.object = Mammals(*args, **kwargs)
        else:
            self.object = Animals(*args, **kwargs)

    def get_object(self):
        return self.object


dog = Fabric(Mammals, False, 'Собака', True).get_object()
print(f'Название: {dog.name}, хвост: {dog.tail}, спячка: {dog.specific()}')

swan = Fabric(Birds, 4, 'Лебедь', True).get_object()
print(f'Название: {swan.name}, хвост: {swan.tail}, длина крыла: {swan.specific()}')

shark = Fabric(Fish, 15, 'Акула', True).get_object()
print(f'Название: {shark.name}, хвост: {shark.tail}, глубина обитания: {shark.specific()}')

viper = Fabric(Animals, 'Гадюка', True).get_object()
print(f'Название: {viper.name}, хвост: {viper.tail}')
