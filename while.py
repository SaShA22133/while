login = "sasha"
parol = "123"
num1 = input(" введите логин ")
num2 = input(" введите пароль ")
while num1 != login or num2 != parol:
    if num1 != login :
        print("Логин не верен")
    if num2 != parol :
        print("пароль не верен")
    num1 = input(" введите логин ")  
    num2 = input(" введите пароль ")
print("вы взломали свой аккаунт")


