# ################################# Polimorfizm ##############################
#
# class Animals:
#     def make_sound(self):
#         raise NotImplemented("Subclass must implement abstract method")
#
# class Dog(Animals):
#     def make_sound(self):
#         return "Bark"
#
# class Cat(Animals):
#     def make_sound(self):
#         return "meaw"
#
# class Cow(Animals):
#     def make_sound(self):
#         return "moo"
#
#
# # фунция работы с полиформизмом
# def animal_sound(animal:Animals):
#     print(animal.make_sound())
#
# dog = Dog()
# cat = Cat()
# cow = Cow()
#
# animal_sound(dog)
# animal_sound(cow)


# class Animal:
#     def make_sound(self):
#         raise NotImplemented("Subclass  must  implement abstract  method")
#
# class Dog(Animal):
#     def make_sound(self):
#         return 'Bark'
#
# class Cat(Animal):
#     def make_sound(self):
#         return 'meow'
#
# class Cow(Animal):
#     def make_sound(self):
#         return 'moo'
#
#
#
#
# #     Функция работы с полиморфизмом
# def animal_sound(animal:Animal):
#     print(animal.make_sound())
#
#
# dog = Dog()
# cat = Cat()
# cow = Cow()
#
# animal_sound(dog)
# animal_sound(cow)

# class Figury:
#
#     def infoFigur(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Kvadrat(Figury):
#     def infoFigur(self):
#         return "имеет 4 угла"
#
# class Treugolnik(Figury):
#     def infoFigur(self):
#         return "имеет 3 угла"
#
# class Krug(Figury):
#     def infoFigur(self):
#         return "не имеет углов"
#
# class Pryamokutnik(Figury):
#     def infoFigur(self):
#         return "тоже имеет 4 стороны, но более широк"
#
# def Figuriki(figury: Figury):
#     print(figury.infoFigur())
#
# krug = Krug()
# kvadrat = Kvadrat()
# pryamokutnik = Pryamokutnik()
#
# Figuriki(kvadrat)
# Figuriki(krug)
# Figuriki(pryamokutnik



