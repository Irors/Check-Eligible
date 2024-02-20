import asyncio
import aiohttp
from add_loguru import logger
from data.datatypes.pypars import ZetaPars
import itertools


def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


def main_opt(wallets: list[str], excel, proxy):

    with open(f'project\\optimism_airdrop4\\winners.txt') as file:
        data = file.readlines()

    for wallet in wallets:
        for account in data:
            if account.split(',')[0] == wallet.lower():
                excel_write(address=wallet.lower(), quantity=account.split(',')[1], excel=excel)
                break
        else:
            excel_write(address=wallet.lower(), quantity=0, excel=excel)


    excel.workbook.save('result/Optimism 4 Airdrop.xlsx')
    logger.info('Check is over. The results are recorded in result')

