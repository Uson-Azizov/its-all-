# class Car():
#     def __init__(self, model, color):
#         self.__model = model
#         self.color = color
#
#     def setter_color(self,new_color):
#         self.color = new_color
#
#     def getter_model(self):
#         return self.__model
#
#     def display_info(self):
#         print(f"model: {self.__model}\n"
#               f"color: {self.color}\n")
#
#
# mers = Car("Mers", "Black")
# print(mers.getter_model())
# mers.setter_color("rad")
# mers.model = "BMW"
# mers.display_info()
from math import atanh


# __model private - закрытый
# _model protected - показанный
# model - открытый


###################################### мурасто #########################################

#
# class Animals:
#     def init(self, name, weight, color, country):
#         self.name = name
#         self.weight = weight
#         self.color = color
#         self.country = country
#
#     def voice(self):
#         print("Animals is voice")
#
#     def sleep(self):
#         print("Animals is sleep")
#
#     def eat(self):
#         print("Animals is eat")
#
#
# class Dog(Animals):
#     def __init__(self, name, weight, color, country, tips, pol):
#         self.name = name
#         self.weight = weight
#         self.color = color
#         self.country = country
#         self.tips = tips
#         self.pol = pol
#
#     def fas(self):
#         print(f"{self.name} is fas")
#
#     def security(self):
#         print(f"{self.name} is security")
#
#
#
# class Cat():
#     def __init__(self,name, weight, color, country, tips, pol):
#         self.name = name
#         self.weight = weight
#         self.color = color
#         self.country = country
#         self.tips = tips
#         self.pol = pol
#
#     def Jump(self):
#         print(f"{self.name} is jump")
#
#     def Let_claws(self):
#         print(f"{self.name} is Let out your claws")
#
#
#
# Animals =Dog("Aktosh", 20, "Black", "Kyrgyzstan", "Pitbul", "man")
# atak = Animals
# Animals.fas()
# atak.voice()
# atak = Cat("Kivi", 21, "white", "Kyrgyzstan", "defolt", "man")
# atak.Jump()
# atak.Let_claws()




class Plants:
    def __init__(self, name, type, color, country):
        self.name = name
        self.type = type
        self.color = color
        self.country = country

    def grow(self):
        print(f"{self.name} is growing")

    def bloom(self):
        print(f"{self.name} is blooming")

    def photosynthesize(self):
        print(f"{self.name} is photosynthesizing")


class Tree(Plants):
    def __init__(self, name, type, color, country, height, lifespan):
        super().__init__(name, type, color, country)
        self.height = height
        self.lifespan = lifespan

    def shed_leaves(self):
        print(f"{self.name} is shedding leaves")

    def provide_shade(self):
        print(f"{self.name} is providing shade")


class Flower(Plants):
    def __init__(self, name, type, color, country, fragrance, petals):
        super().__init__(name, type, color, country)
        self.fragrance = fragrance
        self.petals = petals

    def bloom(self):
        print(f"{self.name} is blooming with {self.petals} petals")

    def release_fragrance(self):
        print(f"{self.name} is releasing {self.fragrance} fragrance")



plant1 = Tree("Oak", "Deciduous", "Green", "USA", 50, 200)
plant2 = Flower("Rose", "Perennial", "Red", "Egypt", "Sweet", 5)


plant1.shed_leaves()
plant1.provide_shade()
plant1.grow()
plant1.photosynthesize()

plant2.bloom()
plant2.release_fragrance()
plant2.grow()
plant2.photosynthesize()





















