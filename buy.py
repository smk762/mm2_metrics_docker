import sys
from decimal import *
from lib_mm2 import mm2
from colprint import colprint

sell_coins = []
available_coins = mm2.list_coins()

for coin in available_coins['enabled']:
    resp = mm2.my_balance(coin)
    bal = resp['balance']
    addr = resp['address']
    if float(bal) > 0:
        sell_coins.append(coin)
    colprint.response(f"{bal} {coin} in {addr}")

colprint.info("Available BUY Coins: "+str(available_coins['enabled']))
colprint.query("Enter coin to BUY: ")
buy_coin = input()

colprint.info("Available SELL Coins: "+str(sell_coins))
colprint.query("Enter coin to SELL: ")
sell_coin = input()

# Show orderbook for pair
orderbook = mm2.orderbook(buy_coin, sell_coin)
for ask in orderbook['asks']:
    max_vol = ask['maxvolume']
    price = ask['price']
    colprint.response(f"{max_vol} {buy_coin} available for {price} {sell_coin}")

colprint.query("Enter BUY price: ")
buy_price = input()

colprint.query("Enter BUY amount: ")
buy_amount = input()

trade_value = Decimal(buy_price)*Decimal(buy_amount)

resp = ''
while resp not in ['y','yes','n','no', 'x']:
    colprint.query(f"CONFIRM [y/n]: BUY {buy_amount} {buy_coin} for {trade_value} {sell_coin}? ")
    resp = input().lower()
    if resp not in ['y','yes','n','no', 'x']:
        colprint.error("Please enter y/n or x to exit!")
if resp == 'x':
    sys.exit()
else:
    buy_resp = mm2.buy(buy_coin, sell_coin, buy_amount, buy_price)
    colprint.response(buy_resp)

