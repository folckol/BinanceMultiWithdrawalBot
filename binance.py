import time
import ccxt
import random
import pandas as pd
from web3 import Web3
# round(random.uniform(0.0098, 0.011), 4)


def binance_withdraw(address, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET):
    account_binance = ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        account_binance.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "network": network
            }
        )
        print(f">>> Успешно | {address} | {amount_to_withdrawal}")
    except Exception as error:
        print(f">>> Неудачно | {address} | ошибка : {error}")


if __name__ == "__main__":

    symbolWithdraw = ''
    network = ''
    amount_to_withdrawal = 0

    # api_keys of binance
    API_KEY = ""
    API_SECRET = ""

    with open('Data/data.txt', 'r') as file:
        for i in file:
            if 'symbol=' in i:
                symbolWithdraw = i.replace('symbol=', '').replace('\n', '')
            elif 'network=' in i:
                network = i.replace('network=', '').replace('\n', '')
            elif 'API_KEY=' in i:
                API_KEY = i.replace('API_KEY=', '').replace('\n', '')
            elif 'API_SECRET=' in i:
                API_SECRET = i.replace('API_SECRET=', '').replace('\n', '')
            elif 'amount_to_withdrawal=' in i:
                amount_to_withdrawal = i.replace('amount_to_withdrawal=', '').replace('\n', '')

    # wallets_list = pd.read_csv('retro.csv').Address.to_list()
    with open("Data/wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]
    # lst = range(4, 5)

    for i in wallets_list:
        address = Web3.to_checksum_address(i)
        binance_withdraw(i, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET)
        time.sleep(random.randint(5, 15))
