import sys
from decimal import *
from lib_mm2 import mm2
from colprint import colprint

log = colprint()

orders = mm2.my_orders()['result']
num_orders = len(orders['maker_orders'])+len(orders['taker_orders'])

if num_orders > 0:
    for order in orders['maker_orders']:
        base = orders['maker_orders'][order]['base']
        rel = orders['maker_orders'][order]['rel']
        amount = Decimal(orders['maker_orders'][order]['available_amount'])
        price = Decimal(orders['maker_orders'][order]['price'])
        total = Decimal(amount*price)
        log.info(f"[MAKER] [{order}] BUY {amount} {rel} at {price} {base} each. (Total: {total} {base})")

    for order in orders['taker_orders']:
        log.info("[TAKER] "+order)


    resp = ''
    while resp not in ['c','p','a', 'u', 'x']:
        log.query("Cancel orders by [U]UIUD, [C]oin, [P]air or [A]ll? ")
        resp = input().lower()
        if resp not in ['c','p','a', 'u', 'x']:
            log.error("Please enter C, P, A, U or X to exit!")

    if resp == 'x':
        sys.exit()

    elif resp == 'a':
        cancel_resp = mm2.cancel_all()

    elif resp == 'c':
        log.query("Enter COIN to cancel: ")
        coin = input()
        cancel_resp = mm2.cancel_coin(coin)

    elif resp == 'p':
        log.query("Enter BASE coin to cancel: ")
        base = input()
        log.query("Enter REL coin to cancel: ")
        rel = input()
        cancel_resp = mm2.cancel_pair(base, rel)

    elif resp == 'u':
        log.query("Enter UUID to cancel: ")
        uuid = input()
        cancel_resp = mm2.cancel_uuid(uuid)

    log.response(cancel_resp)

else:
    log.error("You have no active orders!")

