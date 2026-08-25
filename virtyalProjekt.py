import time

isEnglish = False
users = []
admin_name = ""
password_admin = ""
if isEnglish == True:
    menu_new_user = "1) new user"
    menu_password_correct = "2) change password"
    menu_exit = "3) exit"
    
menu_new_user = "1) новый пользватель"
menu_password_correct = "2) сменить пароль"
menu_exit = "3) выход"

def clr():
    for i in range(50):
        print()
        
def lang_set():
    global isEnglish
    set_tag = True
    while set_tag:
        print("выберите язык:")
        print("1. Русский")
        print("2. English")
        print()
        request_lang = input("> ")
        if request_lang == "1":
            print("успешно!")
            set_tag = False
            clr()
        elif request_lang == "2":
            print("successfully!")
            isEnglish = True
            set_tag = False
            clr()
        else:
            print("input error")
            clr()
            
    
def redakt_password():
    global password_admin
    clr()
    if isEnglish == True:
        request_new_password_ = int(input("new password: "))
        password_admin = request_new_password_
        menu()
    elif isEnglish == False:
        request_new_password_ = int(input("новый пароль: "))
        password_admin = request_new_password_
        menu()
    
def new_users():
    global users
    clr()
    users_conect_ = input("имя нового пользвателя: ")
    users.append(users_conect_)
    print("успешно!")
    print(users)
    menu()
    
def exit_and_entry():
    clr()
    set_tag_1 = True
    set_tag_2 = True
    print("вы вышли с акаунта")
    while set_tag_1:
        request_name_ = input("введите свое имя: ")
        if request_name_ in users:
            set_tag_1 = False
            while set_tag_2:
                clr()
                request_password_ = input("ведите пароль: ")
                if request_password_ == password_admin:
                    set_tag_2 = False
                    menu()
                else:
                    print("не верный пароль")
                    time.sleep(0.8)
                    clr()
        else:
            print("такого пользвателя не сушествует")
            time.sleep(0.8)
            clr()


    
def menu():
    set_menu_tag = True
    users_print = f"пользователи: {', '.join(users)}"
    if isEnglish == True:
        users_print = f"users: {', '.join(users)}"
    while set_menu_tag:
        clr()
        
        print("                       _      _")
        print("#+-+-+-+-+-+-+-+-+-#   |\    /|")
        print("Maks-Virtual-Project   | \  / |")
        print("#+-+-+-+-+-+-+-+-+-#   |  ¯¯  |")
        print("                       —[V][P]—")
        print()
        print(users_print)
        print(menu_new_user)
        print(menu_password_correct)
        print(menu_exit)
        request_ = input("> ")
        if request_ == "1":
            set_menu_tag = False
            new_users()
        if request_ == "2":
            set_menu_tag = False
            redakt_password()
        if request_ == "3":
            set_menu_tag = False
            exit_and_entry()


lang_set()
if isEnglish == True:
    print("Registration is required to use the vertical server")
    request_register_name_admin_ = input("Your Name: ")
    admin_name = request_register_name_admin_
    users.append(admin_name)
    clr()
    request_register_password_admin_ = input(f"fine {admin_name}, Now come up with a strong password: ")
    password_admin = request_register_password_admin_
    print("successfully!")
    clr()
    menu()
    
    
print("чтобы пользватся виртуальным сервером необходимо зарегестрироватся")
request_register_name_admin_ = input("ваше имя: ")
admin_name = request_register_name_admin_
users.append(admin_name)
clr()
request_register_password_admin_ = input(f"хорошо {admin_name}, теперь придумайте надежный пароль: ")
password_admin = request_register_password_admin_
print("успешно!")
clr()
menu()


    
    
    


