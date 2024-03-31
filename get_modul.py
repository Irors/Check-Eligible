import random
from add_loguru import logger

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
 1. [Orbiter Points]
 2. [Mode]
 3. [ZetaChain]
 4. [dappbay]
 5. [Linea-POH]
 6. [DEEP]
\033[m """

    )


try:
    Modul.MODUL = int(input("\033[94m---➜ \033[0m "))
except ValueError:
    logger.error('Write number!')
    exit()

MODULS = {
    1: ('Orbiter Points', main_orbiter),
    2: ('Mode', main_mode),
    3: ('ZetaChain', main_zeta),
    4: ('dappbay', main_dappbay),
    5: ('Linea-POH', main_linea_poh),
    6: ('DEEP', main_deep),
}
