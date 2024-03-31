import asyncio
import aiohttp
from add_loguru import logger
import itertools
import json


async def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def request_send(address: str, json_data: dict, excel, proxy):
    try:
        async with aiohttp.ClientSession(trust_env=True) as session:
            response = await session.post(
                f'https://suiscan.xyz/api/sui-backend/mainnet/api/accounts/{address.lower()}/objects',
                json=json_data,
                proxy='http://' + proxy if proxy else None)

            data = await response.json()
            if '0x61c9c39fd86185ad60d738d4e52bd08bda071d366acde07e07c3916a2d75a816::distribution::DEEPWrapper' in str(
                    data):
                await excel_write(address=address, quantity=True, excel=excel)
            else:
                await excel_write(address=address, quantity=False, excel=excel)

    except Exception as error:
        logger.error(error)


async def make_param(address):
    param = {
        'address': address.lower(),
    }
    return param


async def make_json(address):
    json_data = {
        'objectTypes': [
            'coins',
            'nfts',
            'others',
        ],
    }
    return json_data


async def make_data(address):
    data = f'["{address}"]'
    return data


async def make_request(wallets: list, excel, proxy):
    tasks = [
        request_send(address,
                     await make_json(address),
                     excel,
                     proxy)
        for address in wallets]

    await asyncio.gather(*tasks)


def main_deep(wallets: list[str], excel, proxy):
    if proxy:
        proxy = itertools.cycle(proxy)
    else:
        proxy = itertools.cycle([None])

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(wallets, excel, next(proxy)))

    excel.workbook.save('result/deep.xlsx')
    logger.info('Check is over. The results are recorded in result')
