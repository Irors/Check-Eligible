import asyncio
import aiohttp
from add_loguru import logger
from data.datatypes.pypars import zkLend
import itertools


async def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def request_send(address: str, params: dict, excel, proxy):
    try:
        async with aiohttp.ClientSession(trust_env=True) as session:
            response = await session.get(
                f'https://app.zklend.com/api/airdrop/{address.lower()}',
                proxy='http://' + proxy if proxy else None)

            response = await response.json()
            if response is None:
                await excel_write(address=address, quantity=0,
                                  excel=excel)
            else:
                valueZkLend = zkLend.model_validate(response)
                await excel_write(address=address, quantity=int(valueZkLend.amount.value, 16) / 10**18,
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


def main_zklend(wallets: list[str], excel, proxy):

    if proxy:
        proxy = itertools.cycle(proxy)
    else:
        proxy = itertools.cycle([None])

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(wallets, excel, next(proxy)))

    excel.workbook.save('result/zkLend.xlsx')
    logger.info('Check is over. The results are recorded in result')
