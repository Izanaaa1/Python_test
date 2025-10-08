class User():
    def __init__(self, user_name, last_user_name, passwd):
        self.user_name = user_name
        self.last_user_name = last_user_name
        self.passwd = passwd
    def user_profile(self):
        user_prof = f"\nИмя и фамилия пользователя: {self.user_name.title() + " " + self.last_user_name.title()} \nПароль пользователя: {self.passwd}"
        return user_prof
class Hello_User(User):
    def __init__(self, user_name, last_user_name, passwd):
        super().__init__(user_name, last_user_name, passwd)
    def hello(self):
        print(f"\nЗдравствуйте {self.last_user_name.title() + " " + self.user_name.title()}!")
print("=" * 50)
print("\nРегистрация на сайте")
print("Введите данные и создайте пароль:")
print("\n" + "=" * 50 )
while True:
    # войти в рут права
    root_user = input("Если хотите в root режим нажмите 1, если хотите продолжить регистрацию нажмите любую другую цифру:")
    # проверка на пустую строку
    if root_user == "":
        print("Введите какое нибудь число!")
        continue
    if root_user == "1":
        # Введите пароль 
        while True:
            root_passwd = input("\nВведите пароль:")
            if root_passwd == "": # пароль от 1 до 8
                print("\n\tСтрока не может быть пустой!")
                print("\n\tВведите любое число чтобы продолжить регистрацию без root прав")
                # пробный пароль
            passwd_root_pr = "12345678"
            if root_passwd == passwd_root_pr:
                print("Вы стали root пользователем!")
                break
            elif root_passwd != passwd_root_pr:
                if len(root_passwd) == 1:
                    break
        
    # введите имя
    while True:  
        full_name = input("\nКак вас зовут?:")
        if full_name == "": # Проверка на пустую строку
            print("Имя не может быть пустым")
            continue
        else:
            break
    # введите фамилию
    while True:
        next_name = input("\nКакая ваша фамилия?:")
        if next_name == "":
            print("Фамилия не может быть пустым")
            continue
        else:
            break

    # введите пароль
    while True:
        passw = str(input("\nВведите пароль:")) # введите пароль 
        if len(passw) >= 8: # проверка пароля на количество символов
            break
        else:
            print("В вашем пароле меньше восьми символов, попробуйте еще раз!")
            continue

    break
print("\n" +"=" * 50)


user1 = User(full_name, next_name, passw)
print(user1.user_profile())
hello_user1 = Hello_User(full_name, next_name, passw)
hello_user1.hello()
