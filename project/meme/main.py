from excel.excel import Excel
from project import *
from data.config import *
from .eth import ETHClient
from add_loguru import logger
import itertools
from .meme import meme_m


def main_meme(wallets: list[str], excel, proxy):
    if proxy:
        proxy = itertools.cycle(proxy)
    else:
        proxy = itertools.cycle([None])

    accounts = [ETHClient(private_key, next(proxy)) for private_key in wallets]
    meme_m(accounts=accounts, excel=excel)

