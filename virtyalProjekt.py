
users = []
admin_name = ""
password_admin = 0
menu_new_user = "1) новый пользватель"
menu_password_correct = "2) сменить пароль"
menu_exit = "3) выход"

def redakt_password():
    global password_admin
    request_new_password_ = int(input("новый пароль: "))
    password_admin = request_new_password_
    menu()
    
def new_users():
    global users 
    users_conect_ = input("имя нового пользвателя: ")
    users.append(users_conect_)
    print("успешно!")
    print(users)
    menu()
    
def exit_and_entry():
    print("вы вышли с акаунта")
    while True:
        request_name_ = input("введите свое имя: ")
        if request_name_ in users:
            request_password_ = input("ведите пароль: ")
            if int(request_password_) == password_admin:
                menu()
            else:
                print("не верный пароль")
                request_password_ = input("введите пароль: ")
            
        else:
            print(request_name)
    
def menu():
    print(users)
    print(menu_new_user)
    print(menu_password_correct)
    print(menu_exit)
    request_ = input("> ")
    if request_ == "1":
        new_users()
    if request_ == "2":
        redakt_password()
    if request_ == "3":
        exit_and_entry()
    else:
        menu()

print("здраствуйте")
print("чтобы пользватся виртуальным сервером необходимо зарегестрироватся")
request_register_name_admin_ = input("ваше имя: ")
admin_name = request_register_name_admin_
users.append(admin_name)
request_register_password_admin_ = int(input(f"хорошо {admin_name}, теперь придумайте надежный пароль: "))
password_admin = request_register_password_admin_
print("успешно!")
menu()


    
    
    


