import asyncio
import aiohttp
from add_loguru import logger
from data.datatypes.pypars import ZetaPars
import itertools


async def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def request_send(address: str, params: dict, excel, proxy):
    try:

        headers = {
            'authority': 'xp.cl04.zetachain.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin': 'https://hub.zetachain.com',
            'referer': 'https://hub.zetachain.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }

        async with aiohttp.ClientSession(trust_env=True, headers=headers) as session:
            response = await session.get(
                f'https://xp.cl04.zetachain.com/v1/get-points',
                params=params,
                proxy='http://' + proxy if proxy else None)

            response = await response.json()
            Zeta = ZetaPars.model_validate(response)
            await excel_write(address=address, quantity=Zeta.totalXp if Zeta.totalXp else 0,
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


def main_zeta(wallets: list[str], excel, proxy):

    if proxy:
        proxy = itertools.cycle(proxy)
    else:
        proxy = itertools.cycle([None])

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(wallets, excel, next(proxy)))

    excel.workbook.save('result/ZetaChain.xlsx')
    logger.info('Check is over. The results are recorded in result')
