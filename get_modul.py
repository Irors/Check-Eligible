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
 1. [Alt Layer]
 2. [Orbiter Points]
 3. [Mode]
 4. [Meme]
 5. [Starknet(STRK)]
 6. [ZetaChain]
 7. [Optimism 4 airdrop]
\033[m """

    )


try:
    Modul.MODUL = int(input("\033[94m---➜ \033[0m "))
except ValueError:
    logger.error('Write number!')
    exit()

MODULS = {
    1: ('Alt Layer', main_altlayer),
    2: ('Orbiter Points', main_orbiter),
    3: ('Mode', main_mode),
    4: ('Meme', main_meme),
    5: ('Starknet(STRK)', main_starknet),
    6: ('ZetaChain', main_zeta),
    7: ('Optimism 4 airdrop', main_opt),
}
