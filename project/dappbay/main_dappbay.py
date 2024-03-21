import json
from add_loguru import logger


def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


def main_dappbay(wallets: list[str], excel, proxy):
    with open(f'project\\dappbay\\dappbay.json') as file:
        data = json.load(file)

        for wallet in wallets:
            if wallet.lower() in data['l1'] or wallet.lower() in data['l2']:
                excel_write(address=wallet.lower(), quantity='Eligible', excel=excel)
            else:
                excel_write(address=wallet.lower(), quantity='Non-Eligible', excel=excel)

    excel.workbook.save('result/dappbay.xlsx')
    logger.info('Check is over. The results are recorded in result')
