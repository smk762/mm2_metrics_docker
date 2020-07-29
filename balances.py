import sys
from lib_mm2 import mm2
from colprint import colprint

log = colprint()

if len(sys.argv) > 1:
    coin = sys.argv[1]
else:
    available_coins = mm2.list_coins()
    for coin in available_coins['enabled']:
        resp = mm2.my_balance(coin)
        bal = resp['balance']
        addr = resp['address']
        log.response(f"{bal} {coin} in {addr}")

