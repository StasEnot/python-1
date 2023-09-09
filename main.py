import random
print("Привіт")
input()
print("Як я можу до тебе звертатись?")
Name = input()
print("Дуже приємно, ")
print(Name)
print("Як звати твого кота?")
NameCat = input()
if NameCat == "немає" or NameCat == "немаю":
    print("шкода,")

elif NameCat == "Немає" or NameCat == "Немаю":
    print("Шкода,")

else:
    print(" %s є класним іменем для кота," % NameCat)

print("може ти маєш собаку")
NameDog = input()

if NameDog == "немає" or NameDog == "немаю":
    print("шкода")

elif NameDog == "Немає" or NameDog == "Немаю":
    print("Шкода")

else:
    print(" %s є класним іменем для кота," % NameDog)

for x in range(1,6):
    print("раунд %s" %x)
    print("Ваша відповідь")
    x = input()
    y = random.randint(1,5)
    print("загадине число: %s" %y)
    print()