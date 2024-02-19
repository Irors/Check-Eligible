import loguru

from excel.excel import Excel
from project import *
from data.config import data
from get_modul import MODULS, Modul
from add_loguru import add_logger


def main():
    project, func_run = MODULS[Modul.MODUL]

    with open('data/wallets.txt') as file:
        wallets = [row.strip() for row in file]

    with open('data/proxy.txt') as file:
        proxy = [row.strip() for row in file]

    add_logger()
    loguru.logger.info(f'{project} | Found {len(wallets)} wallets')

    excel = Excel(data)
    eval(f'{func_run.__name__}(wallets={wallets}, excel=excel, proxy=proxy)')


if __name__ == "__main__":
    main()
