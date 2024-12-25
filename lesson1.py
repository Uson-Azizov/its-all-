############################################ while for #####################################################
from array import array
from calendar import weekday
from textwrap import dedent

#пароль от Wifi - dn180323

# range (Start , stop , step)

#
# for i in range (1,10 + 1,1):
#     print (i)
#
#

# text = "python"
# for i in text:
#     print (i)


# for i in range (3):
#     print ("hello")
#

# for i in range(1, 6):
#     if i == 1:
#         continue
#     print (i)

# for d in range(1 , 10+1 ):
#     if d == 5:
#         break
#     print (d)


# for i in range (1, 6+1,1):
#     if i % 2 == 0:
#         print (F"{i} - четное число")
#
#     else:
#         print (f" {i} - нечетное число")


###################################DATA structure  ################################################################



########################################## list ##################################################
# my_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# print (my_list [2])
#
#

# my_list = "hello world"
# print (my_list [-1])
# print (my_list [-2])
# print (my_list [-3])
# print (my_list [-4])
# print (my_list [-5])
# print (my_list [5])
# print (my_list [6])
# print (my_list [7])
# print (my_list [8])
# print (my_list [9])
# print (my_list [10])


#
# my_list = (1,2,3,4,5)
# i = 0
# while i < len (my_list ):
#     print (my_list[i])
#     i = i + 1




# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# print (my_list)


# for i in range(2,10,1):
#     print (i)


#a = ['apple' , 'banana' , 'orange']
#
# for i in a:
#     print (i)

#
# text = ["python"]
# for i in text:
#     print (i)


# for i in range (1,12+1,1):
#     if i % 2 == 0:
#         print (f"{i} - четное")
#
#     else:
#         print (f"{i} - нечетное")
#


# for i in range (1,20+1,1):
#     if i % 2 == 0 :
#         print (f"{i} - chetnoe")
#     else:
#
#         print (f"{i} - nechetnoe")
#


#
# list = (1,4,7,10,15,18,20,25,31,38,40)
# for i  in list:
#     if i == 1:
#         print (f"{i} - минимальные")
#
#     elif i == 40:
#         print (f"{i} - максимальные")
#
#
#


#
# my_list = ["moskva "]
#
# contry = "moskva"
# contry in my_list
# print(f" cтрана найдена   {contry}")
#





#
# list = "Uson,Esentur,Namyz,Kuba,Djapar,"
# my_list = "Beka,Artur,Valik,raika"
# a = list + my_list
# print (a)


#
# a = (1,3,7,8,10,13,15,18,20)
# c = []
# for b in a:
#     if  b >= 10:
#


# a = [1, 3, 7, 8, 10, 13, 15, 18, 20]
# c = [ ]
# i = 0
# while  i < len(a):
#     if a[i] > 10:
#         c.append(a[i])
#     i += 1
# print (f"элементы больше 10 {c}" )
#
# a = int (input ("введите число: "))
# b = int (input ("введите число: "))
# c = int (input ("введите число: "))
# for i  in range(a ,b,c):
#     print (i)
#


#
# list = [1,2,3,4,5]
# n = 0
# for i in list:
#     n += i
# print (n)


##################################################SET#########################################################

# myset = {1,10,2,3,4,5,1,1,2,9}
# myset.add (11)
# print (myset.clear())




############################################# DICTIONARY ############################################################

#mydic = {'name':'Uson','lastname':'Azizov' }

# thidist = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thidist.pop('model')
# print (thidist)
#pop - удаление

# ##################################### keys ##############################################
# thidist = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print (thidist.keys())
#keys - берет ключи (brand , model , year)



###################################### value ##################################################

# thidist = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print (thidist.values())
#values - выводит только те которые внутри ключа (ford , mustang , 1964 )



#a = {b: b for b in range (1, 101)}
#print (a)|
#digit = {}

# for i in range (2,101,2):
#     digit[i] = i + 1
# print(digit)

# mydic = {
#     'apple': 'яблоко',
#     'banana': 'банан',
#     'chery': 'вишня'
# }
#
# word = input ("ведите слова на английском: ")
# translation = mydic.get(word, "слова не найдена")
# print (translation)


#
# people = [
#     {"name": "Tom", "age": 39, "company": "Supercorp", "languages": ["Python", "javaScropt"]},
#     {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "c++", "c#"]},
#     {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "java"]}
# ]
#
# name = input("Введите имя: ").lower()
#
# for digit in people:
#     if digit["name"].lower() == name:
#         print(f"Имя: {digit['name']}")
#         print(f"Возраст: {digit['age']}")
#         print(f"Компания: {digit['company']}")
#         print(f"Языки программирования: {', '.join(digit['languages'])}")
#         break
# else:
#     print(f"{name} - Человек с таким именем не найден")


#
# people = [
#     {"name": "Tom", "age": 39, "company": "Supercorp", "languages": ["Python", "javaScropt"]},
#     {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "c++", "c#"]},
#     {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "java"]}
# ]
# search_name = input("введите имя: ").strip()
# person_data = next((person for person in people if person ['name'].lower() == search_name.lower()), None)
#
# if person_data :
#     print (f"Данные о {search_name}"
#     f"{person_data}")
# else:
#     print (f"{search_name} - Данные о человеке не найдены")




# person = {"name": "Uson", "age": 15, "company": "Digital Nomad", "languages": ["Python"]}
# name = input("Введите: ")
#
# for digit in person:
#     if digit["name"].lower() == name:
#         print(f"Имя: {digit['name']}")
#     else:
#         print ("не правильно")





# a = {"name": "Uson", "age": 15, "company": "Digital Nomad", "languages": ["Python"]}


# b = input("Введите: ")
# if b in a :
#     print (f"данные ключа {a[b]}")
# else:
#     print ("error")


# weekdays = { "ponedelnik":1 , "vtornik":2,
#              "sreda":3 , "chetverk":4,
#              "pytnica":5 , "subbota":6,
#              "voscreseniya":7
# }
# print (weekdays)
#



# 1 - задания


# a = {1:2, 3:4, 5:6}
# print (a.clear())


# 2 - задания

# a = {1:2, 3:4, 5:6}
# print (a.values())



#3 - задания

# a = {"Dima": 40, "Beka": 15, "Esentur": 17}
#
# for b in a:
#     a[b] += 5
# print (a)


############################################## фукнция def ##########################################################

# def uson(name):
#     return f"{name} hello "
#
# print (uson("Uson") )
#
#
#
#
#
#
#
# def digit(lastname , name ,  age, ):
#     return  f"{lastname ,name , age} лет "
# print (digit("Azizov", "uson" ,15  ))
#
#
#
#
# def add_number1 (a,b ):
#      return a + b
# result1 = add_number1(5 , 5)
# rese = add_number1(15 , 15)
# print (result1)
# print (rese)
#
# def add_number (a,b ):
#     return a + b
# result = add_number(2 , 3)
# print (result)
#
#
# def fff():
#     eve = []
#     for digit in range(2, 101, 2):
#         eve.append(digit)
#     return eve
#
# eve = fff()
# print(eve)


# def add(n):
#     for i in range(1,11):
#         print(f'{n}*{i}={i*n}')
#
# add(4)


#

# def DAM(h):
#     return min(h), max (h)
# print(DAM([1,2,3,4]))


# 4 - задания
# def count(n):
#     result = []
#     for num in n:
#         result.append(num * 2)
#     return result
# print(count([4, 2, 100, 3, 10]))

# 5 - задания

# def dad (name , age ):
#     age = 15
#     return f"привет {name} тебе {age} лет ? "
# print (dad('Аня', 23 ))
# print (dad('Петя', 15 ))

# 6 - задания


# def daf (n):
#    return len(set(n))
# print (daf([41,2,13,41,15,1,5,51,51,15,51,51]))


#7 - задания
# def fff(a, operation, b):
#     if operation == "+":
#         print (a + b)
#     elif operation == "-":
#         print (a - b)
#     elif operation == "*":
#         print (a * b)
#     elif operation == "/":
#         print (a / b)
#
# fff(13 , "+" , 31)

# b = [12,3,4,5,6,41,5151,151]
# def dada(b):
#     n=[]
#     for i in b:
#         if i <= 60:
#             n.append(i)
#     return n
# print(dada(b))

# i = (1,2,3,4,5,7,51,16)
# def funk():
#      re = i[0]+i[-1]
#      print (re)
# funk()


#
# a = int (input("Введите четное число: "))
# while True:
#     if a % 2 == 0:
#         print ("это четное число")
#         break
#     else:
#         print ("это не четное число , повторите заново")
#         break

# a = int (input("введите четное число: "))
# if a % 2 == 0:
#     print ("это четное число")
# else:
#     print ("это нечетное число , повторите занова")


# a = input("введите пароль не менее 8 симбволов: ")
# while True:
#     if len(a) < 8:
#         print ("пароль слишком короткий, придумайте новый")
#         break
#     else:
#         print ("Пароль принят!")
#         break
# while True:
#     a = input("введите слово (правильный ответ: python) ")
#     if a == "python":
#         print ("Правильный ответ!")
#         break
#     else:
#         print ("не правильный ответ, повторите снова:")

#
# a = [1,2,3,8,14,85,96]
# print (a[-1])

# while True:
#     a = input("Введите число которое умножается на 3: ")
#     if a % 3 == 0:
#         print ("верно!")
#         break
#     else:
#         print ("неверно, повторите еще!")

############################################ повторение PYTHON ########################################################
# a = int(input("Введите: "))
# b = int(input ("Введите: "))
# c = (a + b)
# print (c)

# a = int(input("Введите a: "))
# oper = int (input("Введите oper: "))
# b = int(input ("Введите b: "))
# if oper == "+":
#     print (a + b)
# elif oper == "-":
#     print (a - b)
# elif oper == "*":
#     print (a * b)
# elif oper == "/":
#     print (a / b)



# for a in range (2,100+1,2):
#     print (f"{a} - четное число")

# age = input ("введите лет: ")
# if age >= 18:
#     print ("совершенолетний")
# else:
#     print ("не совершенно летний")



# a = input ("введите имя")
# print (f"{a} привет ")

# def ddd(a,n):
#     print(a + n)
# ddd(2 , 4)

# for i in range (1,10):
#     print (i)



# a = [1,2,3,4,5,6,7,8,9,10]
# print ([a])



# a = input ("Введите число: ")
# for i in range (1,11):
#     print (f"{a} * {i} = {a*i}")
# a = "hello"
# for b in a:
#     print (b)


# a = int (input ("введите"))
# b = int (input ("введите"))
# c = a + b
# print (c)


######################################## Алгоритмы #####################################################
# сортировка вставка
# def bort(array):
#     lenth = len(array)
#     for i in range (lenth):
#         for j in range (0 , lenth-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#
# array = [3,4,5,1,51,2,3,5,7,8]
# bort(array)
# print(array)

# def bubble_sort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
# number = [5,4,3,6,1,3,51,61,63,5,2,3,51,41,4,2,3,3,7,9,0,]
# print ("исходный массив", number)
# bubble_sort(number)
# print ("отсертованный масив", number)

#
# def investion_sort(arr):
#     for i in range(1,len(arr)):
#         current_value = arr[i]
#         position = i
#         while position > 0 and arr[position - 1] > current_value:
#             arr[position] = arr[position]
#             position -= 1
#             arr[position] = current_value
#     return arr
# numbers = [8,3,1,2,7,5,9]
# print ("до сортировки: ", numbers)
# sorted_numbers = investion_sort(numbers)
# print ("после сортировки:", sorted_numbers )


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i <= 5:
#         print (i)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(filter(lambda elem: elem in b, a))
# print (result)


# a = float(input("Начальная сумма: "))
# b = float(input("процент по вкладу: "))
# c = float(input("Количество лет: "))
# d = (a*b*c)/100
# print ("начисленные проценты:", d)

# a = float(input("введите число: "))
# b = float(input("введите второе число: "))
# if a <= b:
#     print ("наибольшим число является:", b )
# else:
#     print ("наибольшим числом является: ", a)
#молодец!


#
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# g =  a if a>b else b
# print("Наибольшее число: ",g)

#
# a = float(input("введите сумму: "))
# b = float(input("введите скидку: "))
#
# print ("сумма с учетом скидки", a - b)
#
#if a > 0:
#     if a>25000:
#         discount=a * 0.3
#     elif a>15000:
#         discount=a * 0.2
#     elif a>5000:
#         discount = a*0.12
#     else:
#         discount = a*0.05
#     print("Скидка: ", discount)
#     print("Сумма с учетом скидки : ", a-discount)
# else:
#     print("Некорректная сумма")
# a = int(input("Введите сумму продажи: "))

#


##################################### module(MVC) ########################################

# MVC = model , view , controller


######################## oop (object orentions programming)###########################################
#####################  обьектно орентированное програмирование  ######################################



#
# import random
# i = randonm.randint(0,100)
# print(i)

# def hangman(word):
#     wrong = 0
#     stages = ["",
#               "___________           ",
#               "|                     ",
#               "|          |          ",
#               "|          o          ",
#               "|         /|\         ",
#               "|         / \         ",
#               "|                     ",
#               ]
#     rletters = list(word)
#     board = ["__"] * len(word)
#     win = False
#     print("добро пожаловать в игру!")
#     while wrong < len(stages) - 1:
#         print("\n")
#         msg = "введите букву: "
#         char = input(msg)
#         if char in rletters:
#             cind = rletters.index(char)
#             board[cind] = char
#             rletters[cind] = "$"
#         else:
#             wrong += 1
#
#         print((" ".join(board)))
#         e = wrong + 1
#         print("\n".join(stages[0:e]))
#         if "__" not in board:
#             print("Вы выйграли! Было загалано слово: ")
#             print(" ".join(board))
#             win = True
#             break
#     if not win:
#         print("\n".join(stages[0: wrong]))
#         print(f"Вы проиграли! Было загадано слово: {word}")


def hangman(word):
    wrong = 0
    stages = ["",
              "___________           ",
              "|                     ",
              "|          |          ",
              "|          o          ",
              "|         /|\\         ",
              "|         / \\         ",
              "|                     ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать в игру!")
    word = word.lower()

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg).lower()

        if len(char) != 1 or not char.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if char in board:
            print("Вы уже вводили эту букву. Попробуйте снова.")
            continue

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1

        print(" ".join(board))

        e = wrong + 1
        print("\n".join(stages[1:e + 1]))

        if "__" not in board:
            print("Вы выиграли! Было загаданное слово: ")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[1:wrong + 1]))
        print(f"Вы проиграли! Было загадано слово: {word}")



hangman("sico")

















