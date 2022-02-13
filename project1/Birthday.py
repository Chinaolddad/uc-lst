# Imput birthdaye calculating Age

import datetime
name = str(input("what is your name?"))
birth_day = int(input("What is your birth year?"))
age = datetime.date.today().year - birth_day

print("Hello, "+ str(name) + " !. You are " + str(age) + " years old")

