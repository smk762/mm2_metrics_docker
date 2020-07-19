import sys
from decimal import *
from lib_mm2 import mm2
from colprint import colprint

orders = mm2.my_orders()['result']
num_orders = len(orders['maker_orders'])+len(orders['taker_orders'])

if num_orders > 0:
    for order in orders['maker_orders']:
        base = orders['maker_orders'][order]['base']
        rel = orders['maker_orders'][order]['rel']
        amount = Decimal(orders['maker_orders'][order]['available_amount'])
        price = Decimal(orders['maker_orders'][order]['price'])
        total = Decimal(amount*price)
        colprint.info(f"[MAKER] [{order}] BUY {amount} {rel} at {price} {base} each. (Total: {total} {base})")

    for order in orders['taker_orders']:
        colprint.info("[TAKER] "+order)


    resp = ''
    while resp not in ['c','p','a', 'u', 'x']:
        colprint.query("Cancel orders by [U]UIUD, [C]oin, [P]air or [A]ll? ")
        resp = input().lower()
        if resp not in ['c','p','a', 'u', 'x']:
            colprint.error("Please enter C, P, A, U or X to exit!")

    if resp == 'x':
        sys.exit()

    elif resp == 'a':
        cancel_resp = mm2.cancel_all()

    elif resp == 'c':
        colprint.query("Enter COIN to cancel: ")
        coin = input()
        cancel_resp = mm2.cancel_coin(coin)

    elif resp == 'p':
        colprint.query("Enter BASE coin to cancel: ")
        base = input()
        colprint.query("Enter REL coin to cancel: ")
        rel = input()
        cancel_resp = mm2.cancel_pair(base, rel)

    elif resp == 'u':
        colprint.query("Enter UUID to cancel: ")
        uuid = input()
        cancel_resp = mm2.cancel_uuid(uuid)

    colprint.response(cancel_resp)

else:
    colprint.error("You have no active orders!")

