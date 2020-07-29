import sys
from lib_mm2 import mm2
from colprint import colprint

available_coins = mm2.list_coins()

log = colprint()

if len(sys.argv) > 1:
    coin = sys.argv[1]
else:
    log.info("Enabled coins: "+str(available_coins['enabled']))
    log.info("Inactive coins: "+str(available_coins['inactive']))
    log.query("Enter coin to activate: ")
    coin = input()

if coin in available_coins['inactive']:
    log.info("Activating "+coin)
    log.response(mm2.electrum(coin))
elif coin in available_coins['enabled']:
    log.warn(coin+" already active!")
    log.response(mm2.my_balance(coin))
else:
    log.warn("Coin not in available coins list!")
    log.info("Inactive coins: "+str(available_coins['inactive']))


