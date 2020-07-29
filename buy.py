import sys
from decimal import *
from lib_mm2 import mm2
from colprint import colprint

log = colprint()

sell_coins = []
available_coins = mm2.list_coins()

for coin in available_coins['enabled']:
    resp = mm2.my_balance(coin)
    bal = resp['balance']
    addr = resp['address']
    if float(bal) > 0:
        sell_coins.append(coin)
    log.response(f"{bal} {coin} in {addr}")

log.info("Available BUY Coins: "+str(available_coins['enabled']))
log.query("Enter coin to BUY: ")
buy_coin = input()

log.info("Available SELL Coins: "+str(sell_coins))
log.query("Enter coin to SELL: ")
sell_coin = input()

# Show orderbook for pair
orderbook = mm2.orderbook(buy_coin, sell_coin)
for ask in orderbook['asks']:
    max_vol = ask['maxvolume']
    price = ask['price']
    log.response(f"{max_vol} {buy_coin} available for {price} {sell_coin}")

log.query("Enter BUY price: ")
buy_price = input()

log.query("Enter BUY amount: ")
buy_amount = input()

trade_value = Decimal(buy_price)*Decimal(buy_amount)

resp = ''
while resp not in ['y','yes','n','no', 'x']:
    log.query(f"CONFIRM [y/n]: BUY {buy_amount} {buy_coin} for {trade_value} {sell_coin}? ")
    resp = input().lower()
    if resp not in ['y','yes','n','no', 'x']:
        log.error("Please enter y/n or x to exit!")
if resp == 'x':
    sys.exit()
else:
    buy_resp = mm2.buy(buy_coin, sell_coin, buy_amount, buy_price)
    log.response(buy_resp)

