import loguru

from excel.excel import Excel
from project import *
from data.config import *
from get_modul import MODULS, Modul
from add_loguru import add_logger


def main():

    project, func_run = MODULS[Modul.MODUL]

    with open('data/wallets_evm.txt') as file:
        wallets = [row.strip() for row in file]

    add_logger()
    loguru.logger.info(f'Found {len(wallets)} wallets')

    excel = Excel(eval(f'{func_run.__name__}_data'))
    eval(f'{func_run.__name__}(wallets={wallets}, excel=excel)')


if __name__ == "__main__":
    main()
