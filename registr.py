def list_person(info_person):

    return f"Пользователь {person["Name"]} {person["next_name_l"]}"
"""Регистрация на сайт"""
while True:
    # Введите имя и фамилию
    print("="*50)
    print("Регистрация на сайте")
    print("Введите данные и создайте пароль:")
    print("="*50)

    
    full_name = input("\nКак вас зовут?:")
    if full_name == "": # Проверка на пустую строку
        print("Имя не может быть пустым")
        continue

    
    next_name = input("\nКакая ваша фамилия?:")
    if next_name == "":
        print("Фамилия не может быть пустым")
        
        continue


    while True:
        passw = str(input("\nВведите пароль:")) # введите пароль 
        if len(passw) >= 8: # проверка пароля на количество символов
            break
        else:
            print("В вашем пароле меньше восьми символов, попробуйте еще раз!")
            continue

    break
print("=" * 100)

person = {
    "Name":full_name,
    "next_name_l":next_name, 
    "passord":passw
        }
text = list_person(person)
print(text)
print("\nЗдравствуйте", person["Name"], person["next_name_l"], "!")
    
