from web3 import Web3
from eth_account.messages import encode_defunct
from eth_account import Account
web3 = Web3(Web3.HTTPProvider('https://ethereum.publicnode.com'))


class ETHClient:

    def __init__(self, private, proxy):

        self.private_key = private
        self.address = web3.eth.account.from_key(self.private_key).address
        self.message = f"The wallet will be used for MEME allocation. If you referred friends, family, lovers or strangers, ensure this wallet has the NFT you referred.\n\nBut also...\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWallet: {self.address[:5]}...{self.address[-4:]}"
        self.proxy = proxy
        self.signature = get_signature(private_key=self.private_key,
                                       message=f"The wallet will be used for MEME allocation. If you referred friends, family, lovers or strangers, ensure this wallet has the NFT you referred.\n\nBut also...\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWallet: {self.address[:5]}...{self.address[-4:]}")


def get_signature(private_key, message) -> str:
    return Account.sign_message(signable_message=encode_defunct(
            text=message),
            private_key=private_key).signature.hex()

