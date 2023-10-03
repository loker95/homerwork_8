import re


user_home_number = input("Введите домашний номер ")


def validate_home_number(number):
    if re.match(r'[0-9]{7}', number) and len(number) == 7:
        print("Верный номер ")
    else:
        print("Неверный номер ")


validate_home_number(user_home_number)


user_mob_number = input("Введите мобильный номер ")


def validate_mob_number(number):
    if re.match(r'^(\+\d{12}|\d{12})$', number):
        print("Верный номер ")
    else:
        print("Неверный номер ")


validate_mob_number(user_mob_number)


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        print("это корректный email-адрес. ")
    else:
        print("это некорректный email-адрес. ")


email = input("vvedite email ")

validate_email(email)


user_full_name = input("Введите ФИО ")


def validate_full_name(full_name):
    pattern = r'^[а-яА-Яa-zA-Z]{2,20}\s[а-яА-Яa-zA-Z]{2,20}\s[а-яА-Яa-zA-Z]{2,20}$'

    if re.match(pattern, full_name):
        print("Это корректное ФИО ")
    else:
        print("Некорректное ФИО ")


validate_full_name(user_full_name)

