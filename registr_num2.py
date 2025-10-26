from cryptography.fernet import Fernet
import os
import maskpass
from dotenv import load_dotenv
class User():
    def __init__(self, user_name, last_user_name, passwd):
        self.user_name = user_name
        self.last_user_name = last_user_name
        self.passwd = passwd
    def user_profile(self):
        user_prof = f"\nИмя и фамилия пользователя: {self.user_name.title() + " " + self.last_user_name.title()} \nПароль пользователя: {self.passwd}"
        return user_prof
class Admin():
    def __init__(self, name_admin, last_name_admin, email="igramm586@gmail.com"):
        self.privil_admin = [
            "Удалять и добавлять участников",
            "Банить участников", 
            "Изменять данные на сайте"
        ]
        self.name_admin = name_admin
        self.last_name_admin = last_name_admin
        self.email = email
    
    def prof_admin(self):
        return f"ФИО Админа: {self.last_name_admin} {self.name_admin}\nПочта поддержки: {self.email}"
    
    def hello_admin(self):
        greeting = f"Здравствуйте {self.last_name_admin.title()} {self.name_admin.title()}!"
        print(greeting)
        return greeting
    
    def priveleg(self): 
        print("Привилегии админа:")
        for priv in self.privil_admin:
            print(f"- {priv}")
print("=" * 50)
print("\nРегистрация на сайте")
print("Введите данные и создайте пароль:")
print("\n" + "=" * 50 )
while True:
     
    try:
        root_user = int(input("Если хотите вы администратор нажмите 1, если хотите продолжить регистрацию нажмите любую другую цифру:"))
    except ValueError:
        print("Вы ввели не число!")
        continue
    else:
        break
admin_online = False
while True:
    # проверка на пустую строку
    if root_user == "":
        print("Введите какое нибудь число!")
        continue
    if root_user == 1:
        for i in range(3, -1, -1):

            print("\n")
            root_passwd = maskpass.advpass("Введите пароль:")
            if root_passwd == "": # пароль от 1 до 8
                print("\n\tСтрока не может быть пустой!")
                print("\n\tВведите любое число чтобы продолжить регистрацию как пользователь")
                print(f"\n\tУ вас осталось еще {i} попытки")
                continue
                    # пробный пароль
            psw = os.getenv("TOKEN")
            if root_passwd == psw:
                print("Успешно!")
                admin_online = True
                break
            elif root_passwd != psw:
                print(f"\n\tУ вас осталось еще {i} попытки")
                if len(root_passwd) == 1:
                    admin_online = False
                    break
                
                
    break           
                
if root_user != '1':
        """Ввод имени пользователя"""
    # введите имя
while True: 
        if admin_online:
            break
        full_name = input("\nКак вас зовут?:")
        if full_name == "": # Проверка на пустую строку
            print("Имя не может быть пустым")
            continue
        else:
            break
            # введите фамилию
while True:
        if admin_online:
            break
        next_name = input("\nКакая ваша фамилия?:")
        if next_name == "":
            print("Фамилия не может быть пустым")
            continue
        else:
            break


            # введите пароль
while True:
        if admin_online:
            break
        passw = maskpass.advpass("Введите пароль:") # введите пароль 
        if len(passw) >= 8: # проверка пароля на количество символов
            break
    
        else:
            print("В вашем пароле меньше восьми символов, попробуйте еще раз!")
            continue   
print("\n" +"=" * 50)


if admin_online:
    admin = Admin("Играми", "Рамазанов")
    print(admin.prof_admin())
    admin.hello_admin()
    admin.priveleg()
    
if admin_online == False:
        
        user1 = User(full_name, next_name, passw)
        print(user1.user_profile())
        key = Fernet.generate_key()
        chiper = Fernet(key)
        encrypted = chiper.encrypt(passw.encode())
        with open("log_user.txt", "a") as log_file:
            log_file.write(f"\nПользователь:{full_name.title() + " " + next_name.title()}\nПароль пользователя:{encrypted}\n")

