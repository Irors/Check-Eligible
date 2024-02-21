import asyncio
import aiohttp
from add_loguru import logger
from .eth import ETHClient


async def excel_write(address: str, quantity, excel):
    data = [address, quantity]
    excel.sheet.append(data)


async def get_points(account: str):
    async with aiohttp.ClientSession(headers={
        'authority': 'memefarm-api.memecoin.org',
        'accept': 'application/json',
        'accept-language': 'ru',
        'authorization': 'Bearer ' + account.accessToken,
        'origin': 'https://www.memecoin.org',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }, trust_env=True) as session:
        response = await session.get('https://memefarm-api.memecoin.org/user/tasks',
                                     proxy='http://' + str(account.proxy))
        result = await response.json(content_type=None)
        return result['points']['current']


async def request_send_info_bots(account: str, excel):
    async with aiohttp.ClientSession(headers={
        'authority': 'memefarm-api.memecoin.org',
        'accept': 'application/json',
        'accept-language': 'ru',
        'authorization': 'Bearer ' + account.accessToken,
        'origin': 'https://www.memecoin.org',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }, trust_env=True) as session:
        response = await session.get('https://memefarm-api.memecoin.org/user/results',
                                     proxy='http://' + str(account.proxy))
        result = await response.json(content_type=None)

        await excel_write(address=account.address, quantity='ROBOT' if result['results'][0]['won'] == False else
        await get_points(account), excel=excel)


async def request_send_access(account: str, json_data: dict, excel):
    async with aiohttp.ClientSession(headers={'origin': 'https://www.memecoin.org',
                                              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'},
                                     trust_env=True) as session:

        response = await session.post('https://memefarm-api.memecoin.org/user/wallet-auth', json=json_data,
                                      proxy='http://' + str(account.proxy))

        result = await response.json(content_type=None)
        if 'unauthorized' in str(result):
            account.accessToken = 0
        else:
            account.accessToken = result['accessToken']
            await request_send_info_bots(account=account, excel=excel)


async def make_param(address):
    param = {
        'address': address.lower(),
    }
    return param


async def make_json(account):
    json_data = {
        'address': account.address,
        'delegate': account.address,
        'message': account.message,
        'signature': account.signature
    }
    return json_data


async def make_request(accounts: list, excel):
    tasks = [
        request_send_access(account,
                            await make_json(account),
                            excel)
        for account in accounts]

    await asyncio.gather(*tasks)


def meme_m(accounts: list[ETHClient], excel):
    logger.info(f"I'm starting to check the accounts for ROBOT/HUMAN...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.set_event_loop(loop)
    loop.run_until_complete(make_request(accounts, excel))

    logger.info(r'Check is over. The results are recorded in result')
    excel.workbook.save('result/Meme.xlsx')
