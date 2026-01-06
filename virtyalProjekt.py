T = 0
QQ = 0
w = ""
users = []
password = QQ
admin = w
menu0 = "1)новый пользватель"
menu1 = "2)сменить пароль"
menu2 = "3)выход"
def redaktPassword():
    global T, password
    T = int(input("новый пароль: "))
    password = T
    menu()
    
def newUSers():
    global users 
    E = input("имя нового пользвателя: ")
    users.append(E)
    print("успешно!")
    print(users)
    menu()
    
def expt():
    print("вы вышли с акаунта")
    while True:
        S = input("введите свое имя: ")
        if S in users:
            SS = input("ведите пароль: ")
            if int(SS) == password:
                menu()
            else:
                print("не верный пароль")
                SS = input("введите пароль: ")
        if S == admin:
            SS = input("ведите пароль: ")
            
        else:
            print(S)
    
def menu():
    print(users)
    print(menu0)
    print(menu1)
    print(menu2)
    QQQ = input("> ")
    if QQQ == "1":
        newUSers()
    if QQQ == "2":
        redaktPassword()
    if QQQ == "3":
        expt()
    else:
        menu()

print("здраствуйте")
print("чтобы пользватся виртуальным сервером необходимо зарегестрироватся")
Q = input("ваше имя: ")
admin = Q
users.append(admin)
QQ = int(input(f"хорошо {admin},теперь придумайте надежный пароль: "))
password = QQ
print("успешно!")
menu()


    
    
    


