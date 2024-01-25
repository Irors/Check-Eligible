import loguru

from excel.excel import Excel
from project import *
from data.config import *
import questionary
from add_loguru import add_logger


def main():
    answer = questionary.select(
        "What do you want to do?",
        choices=[
            "altlayer"
        ],
        pointer='►'
    ).ask()

    with open('data/wallets_evm.txt') as file:
        wallets = [row.strip() for row in file]

    add_logger()
    loguru.logger.info(f'Found {len(wallets)} wallets')

    excel = Excel(eval(f'{answer}_data'))
    eval(f'main_{answer}(wallets={wallets}, excel=excel)')


if __name__ == "__main__":
    main()
