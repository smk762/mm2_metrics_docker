import sys
from lib_mm2 import mm2
from colprint import colprint

available_coins = mm2.list_coins()

if len(sys.argv) > 1:
    coin = sys.argv[1]
else:
    colprint.info("Enabled coins: "+str(available_coins['enabled']))
    colprint.info("Inactive coins: "+str(available_coins['inactive']))
    colprint.query("Enter coin to activate: ")
    coin = input()

if coin in available_coins['inactive']:
    colprint.info("Activating "+coin)
    colprint.response(mm2.electrum(coin))
elif coin in available_coins['enabled']:
    colprint.warn(coin+" already active!")
    colprint.response(mm2.my_balance(coin))
else:
    colprint.warn("Coin not in available coins list!")
    colprint.info("Inactive coins: "+str(available_coins['inactive']))


