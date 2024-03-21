import asyncio
import aiohttp
from add_loguru import logger
from data.datatypes.pypars import nim
import itertools


async def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def request_send(address: str, params: dict, excel, proxy):
    try:

        async with aiohttp.ClientSession(
                headers={
                    'accept': '*/*',
                    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                    'access-control-allow-origin': '*',
                    'origin': 'https://claim.nim.network',
                    'referer': 'https://claim.nim.network/',
                    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                },
                trust_env=True) as session:

            response = await session.post(
                f'https://claim-apis.nim.network/{address.lower()}')

            response = await response.json()
            if 'amount' in str(response):
                NIM = nim.model_validate(response)
                await excel_write(address=address, quantity=NIM.amount,
                                  excel=excel)
            else:
                await excel_write(address=address, quantity=0,
                                  excel=excel)

    except Exception as error:
        logger.error(error)


async def make_param(address):
    param = {
        'address': address.lower(),
    }
    return param


async def make_json(address):
    json_data = {
        'address': address.lower(),
    }
    return json_data


async def make_data(address):
    data = f'["{address}"]'
    return data


async def make_request(wallets: list, excel, proxy):
    tasks = [
        request_send(address,
                     await make_param(address),
                     excel,
                     proxy)
        for address in wallets]

    await asyncio.gather(*tasks)


def main_nim(wallets: list[str], excel, proxy):

    if proxy:
        proxy = itertools.cycle(proxy)
    else:
        proxy = itertools.cycle([None])

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(wallets, excel, next(proxy)))

    excel.workbook.save('result/nim.xlsx')
    logger.info('Check is over. The results are recorded in result')
