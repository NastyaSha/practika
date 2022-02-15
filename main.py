name = "Анастасия"  # задание 1,2,3
age = 19
print("Мое имя:", name, "Возраст:", str(age))

myname = name + " " + name + " " + name + " " + name + " " + name
print(myname)

name = input("Ваше имя(задание 4)")  # задание 4

age = str(input("Возраст(задание 4)"))

print("Здравствуйте", name, "! \n Вам", age, "?", "Вы никогда не интересовались домом престорелых?")

#---------------------------------------------------------------

age1 = int(input("Ваш возраст(задание 5)"))  # задание 5

if age1 >= 18 and age1 <= 50:
    print("Пора на покой")

elif age1 >= 50:
    print("Ты крут")

else:
    print("Персик дозревай")

name = input("Ваше Имя")
#---------------------------------------------------------------

name2 = input("Ваше имя(задание 6,7,8,9,10)")

if len(name2) < 5:
    print("Введите другое имя больше 5", name2[::-1])

else:
    a = len(name2)
    print(name2[1:], name2[-3:], name2[::-1], name2[:5]) #задание 6

age = int(input("Возраст(задание 6,7,8,9,10)"))#задание 7
sumi = 0
pro = 1
while age != 0:
    sumi = sumi + age % 10
    pro *= age % 10
    age = age // 10

print(sumi, len(name2), pro)

if int(input("Сколько будет 2+2?")) == 4: #задание 10
    print(name2.lower(), name2.upper(), name2.capitalize(), name2.swapcase()) #задание 8

age1 = int(input("Ваш возраст"))

if (" " in name2) or (age1 < 0) or (age1 > 150): # задание 9
    print("ошибка")