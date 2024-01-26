import asyncio
import aiohttp
from add_loguru import logger
from data.datatypes.pypars import OrbiterPars
import itertools


async def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def request_send(address: str, params: dict, excel, semaphore, proxy):
    try:

        async with aiohttp.ClientSession() as session:
            await semaphore.acquire()
            response = await session.get(
                f'https://api.orbiter.finance/points_system/v2/user/points',
                params=params,
                proxy='http://' + proxy if proxy else None)

            response = await response.json()
            Orbiter = OrbiterPars.model_validate(response)
            await excel_write(address=address, quantity=Orbiter.data.total,
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


async def make_request(wallets: list, excel, semaphore, proxy):
    tasks = [
        request_send(address,
                     await make_param(address),
                     excel,
                     semaphore,
                     proxy)
        for address in wallets]

    await asyncio.gather(*tasks)


def main_orbiter(wallets: list[str], excel, proxy):

    if proxy:
        proxy = itertools.cycle(proxy)
    else:
        proxy = itertools.cycle([None])

    semaphore = asyncio.Semaphore(value=200)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(wallets, excel, semaphore, next(proxy)))

    excel.workbook.save('result/Orbiter.xlsx')
    logger.info('Check is over. The results are recorded in result')
