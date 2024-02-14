import json
from add_loguru import logger


def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


def main_starknet(wallets: list[str], excel, proxy):
    for i in range(7):
        with open(f'project\\starknet\\starknet-{i}.json') as file:
            data = json.load(file)

        for account in data['eligibles']:
            for wallet in wallets:
                if account['identity'] == wallet.lower():
                    excel_write(address=wallet.lower(), quantity=account['amount'], excel=excel)

    excel.workbook.save('result/Starknet.xlsx')
    logger.info('Check is over. The results are recorded in result')
