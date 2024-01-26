import random
from project import *

RANDOM_PREFIX = [
    f"\033[{random.randint(30, 37)}m" + \
    "  _____  _  _         _  _      _           ___  \n" + \
    " | ____|| |(_)  __ _ (_)| |__  | |  ___    |__ \ \n" + \
    " |  _|  | || | / _` || || '_ \ | | / _ \     / / \n" + \
    " | |___ | || || (_| || || |_) || ||  __/    |_|  \n" + \
    " |_____||_||_| \__, ||_||_.__/ |_| \___|    (_)  \n" + \
    "               |___/                             \n"
]
print(random.choice(RANDOM_PREFIX))


class Modul:
    MODUL = None
    print(
        f"""\033[36m Developed by @Irorsss \033[m
         \033[96m
 1. [Alt Layer]
 2. [Orbiter Points]
\033[m """

    )


Modul.MODUL = int(input("\033[94m---➜ \033[0m "))

MODULS = {
    1: ('Alt Layer', main_altlayer),
    2: ('Orbiter Points', main_orbiter)
}
