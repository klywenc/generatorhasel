import sys
import random
import string
import mysql.connector

password = []
chara_left = -1


def update_charaters_left(number_of_chara):
    global chara_left

    if number_of_chara < 0 or number_of_chara > chara_left:
        print("Przekroczono liczbę znaków")
        sys.exit(0)
    else:
        chara_left -= number_of_chara
        print("Pozostało znaków", chara_left)


password_leng = int(input("podaj długość hasła"))

if password_leng <= 5:
    print("twoje twoje hasło będzie za krótkie")
    sys.exit(0)
else:
    chara_left = password_leng

uppercase_letters = int(input("ile dużych liter"))
update_charaters_left(uppercase_letters)

lowercase_letters = int(input("ile malych liter?"))
update_charaters_left(lowercase_letters)

special_chara = int(input("Znaki specjalne"))
update_charaters_left(special_chara)

digi = int(input("Cyfry"))
update_charaters_left(digi)

aplikacja = str(input("Podaj nazwę aplikacji do której chcesz przypisać hasło"))

if chara_left > 0:
    print("Nie wykorzystano wszystkich przewidzianych znakow hasło zostanie uzupełnione małymi literami")
    lowercase_letters += chara_left
print()
print("Długość Hasła", password_leng)
print("Małe litery", lowercase_letters)
print("Duże litery", uppercase_letters)
print("Znaki specjalne", special_chara)
print("Cyfry", digi)

for i in range(password_leng):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_chara > 0:
        password.append(random.choice(string.punctuation))
        special_chara -= 1
    if digi > 0:
        password.append(random.choice(string.digits))
        digi -= 1

random.shuffle(password)
file = open("haslo.txt", "a")
print("Wygenerowane hasło:", "".join(password))
file.write(str(aplikacja) + " - " + str("".join(password)))
file.close()

connection = mysql.connector.connect(user='root', password='', host='127.0.0.1')
database = aplikacja, auth_plugin='mysql_native_password'
cursor = connection.cursor()

query = "INSERT INTO aplikacja(Aplikacja, password) VALUES(%(Aplikacja)s, %(password)s)"
insertData = {
    'Aplikacja' : aplikacja,
    'password' : str("".join(password))
}
cursor.execute(insertQuery, insertData)









