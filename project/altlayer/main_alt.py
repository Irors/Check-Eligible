import asyncio
import aiohttp
import json
from web3 import Web3
from add_loguru import logger
from data.datatypes.altlayerdt import AltLayerPars


async def excel_write(address: str, quantity: float, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def request_send(address: str, data: str, excel, semaphore):
    try:
        headers = {
            'next-action': '6817e8f24aae7e8aed1d5226e9b368ab8c1ded5d',
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            await semaphore.acquire()
            response = await session.post(
                f'https://airdrop.altlayer.io/', data=data)

            text = await response.text()

            if len(text) > 100:
                result = json.loads(str(text).split(':', 2)[2])
                AltLayer = AltLayerPars.model_validate(result)
                await excel_write(address=AltLayer.address, quantity=(float(AltLayer.amount) / 10 ** 18),
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
    web3 = Web3(Web3.HTTPProvider('https://ethereum.publicnode.com'))
    data = f'["{web3.to_checksum_address(address)}"]'
    return data


async def make_request(wallets: list, excel, semaphore):
    tasks = [
        request_send(address,
                     await make_data(address),
                     excel,
                     semaphore)
        for address in wallets]

    await asyncio.gather(*tasks)


def main_altlayer(wallets: list[str], excel):
    semaphore = asyncio.Semaphore(value=200)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(wallets, excel, semaphore))

    excel.workbook.save('result/AltLayer.xlsx')
    logger.info('Check is over. The results are recorded in result/AltLayer.xlsx')
