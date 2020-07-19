#!/usr/bin/env python3
import os
import sys
import json
import time
import requests
from os.path import expanduser

cwd = os.getcwd()
script_path = sys.path[0]
home = expanduser("~")

# Get credentials from MM2.json
with open("./mm2/MM2.json") as f:
    mm2_creds = json.loads(f.read())

with open("./mm2/coins") as f:
    mm2_coins = json.loads(f.read())
    coins = []
    for item in mm2_coins:
        if 'mm2' in item:
            if item['mm2'] == 1:
                coins.append(item)

electrums = {}
r = requests.get('http://stats.kmd.io/api/info/coins/?mm2_compatible=1')
coins_info = r.json()['results'][0]
for coin in coins_info:
    if 'electrums' in coins_info[coin]:
        if len(coins_info[coin]['electrums']) > 0:
            electrums.update({coin:coins_info[coin]['electrums']})
    elif 'etomic' in coins_info[coin]:
        electrums.update({coin:["http://eth1.cipig.net:8555",
                                "http://eth2.cipig.net:8555",
                                "http://eth3.cipig.net:8555"]
                        })

class mm2_proxy:
    '''
    Class for accessing mm2 methods
    '''
    def __init__(self, coins, userpass, node_ip):
        self.coins = coins
        self.userpass = userpass
        self.node_ip = "http://"+node_ip+":7783"
        self.params = {'userpass': self.userpass}

    def buy(self, base, rel, basevolume, relprice):
        self.params.update({
                     'method': 'buy',
                     'base': base,
                     'rel': rel,
                     'volume': basevolume,
                     'price': relprice
                 })
        r = requests.post(self.node_ip,json=self.params)
        return r.json()    


    def cancel_all(self):
        self.params.update({
                  'method': 'cancel_all_orders',
                  'cancel_by': {"type":"All"}})
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def cancel_coin(self, coin):
        self.params.update({
                  'method': 'cancel_all_orders',
                  'cancel_by': {
                        "type":"Coin",
                        "data":{"ticker":coin},
                        }})
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def cancel_pair(self, base, rel):
        self.params.update({
                  'method': 'cancel_all_orders',
                  'cancel_by': {
                        "type":"Pair",
                        "data":{"base":base,"rel":rel},
                        }})
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def cancel_uuid(self, order_uuid):
        self.params.update({
                  'method': 'cancel_order',
                  'uuid': order_uuid})
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def coins_needed_for_kick_start(self):
        pass

    def disable_coin(self):
        pass

    def electrum(self, cointag, tx_history=True):
        if cointag in coins_info:
            if 'etomic' in coins_info[cointag]['coins_info']:
                self.params.update({
                          'method': 'enable',
                          'urls':["http://eth1.cipig.net:8555",
                                  "http://eth2.cipig.net:8555",
                                  "http://eth3.cipig.net:8555"],
                          'coin': cointag,
                          'swap_contract_address': '0x8500AFc0bc5214728082163326C2FF0C73f4a871',
                          'mm2':1,
                          'tx_history':tx_history})
            else:
                electrums = []
                for server in coins_info[cointag]['electrums']:
                    electrums.append({"url":server})
                if len(electrums) > 0:
                    self.params.update({
                              'method': 'electrum',
                              'servers':electrums,
                              'coin': cointag,
                              'mm2':1,
                              'tx_history':tx_history})
                else:
                    print(coin+" has no electrums defined!")
                    return False
            r = requests.post(self.node_ip, json=self.params)
            return r.json()
        else:
            print(coin+" has no info!")
            return False

    def enable(self, cointag, tx_history=True):
        coin = coinslib.coins[cointag]
        self.params.update({
                  'method': 'enable',
                  'coin': cointag,
                  'mm2':1,  
                  'tx_history':tx_history})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def get_enabled_coins(self):
        self.params.update({'method': 'get_enabled_coins'})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def get_enabled_coins_list(self):
        self.params.update({'method': 'get_enabled_coins'})
        r = requests.post(self.node_ip, json=self.params)
        enabled_coins = []
        for item in r.json()['result']:
            enabled_coins.append(item['ticker'])
        return enabled_coins

    def get_trade_fee(self, coin):
        self.params.update({
                  'method': 'get_trade_fee',
                  'coin': coin
                  })
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def help(self):
        self.params.update({'method': 'help'})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def import_swaps(self):
        pass

    def list_banned_pubkeys(self):
        pass

    def max_taker_vol(self):
        pass

    def my_balance(self, cointag):
        self.params.update({
                  'method': 'my_balance',
                  'coin': cointag})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def my_orders(self):
        self.params.update({'method': 'my_orders'})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def my_recent_swaps(self, limit=10, from_uuid=''):
        if from_uuid=='':
            self.params.update({
                      'method': 'my_recent_swaps',
                      'limit': int(limit)})
            
        else:
            self.params.update({
                      'method': 'my_recent_swaps',
                      "limit": int(limit),
                      "from_uuid":from_uuid})
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def my_swap_status(self, swap_uuid):    
        self.params.update({
                  'method': 'my_swap_status',
                  'params': {"uuid": swap_uuid}})
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def my_tx_history(self):
        pass

    def order_status(self):
        pass

    def orderbook(self, base, rel):
        self.params.update({
                     'method': 'orderbook',
                     'base': base,
                     'rel': rel
                 })
        r = requests.post(self.node_ip,json=self.params)
        return r.json()

    def recover_funds_of_swap(self, uuid):
        self.params.update({
                  'method': 'recover_funds_of_swap',
                  'params': {'uuid':uuid}
                  })
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def sell(self):
        pass

    def send_raw_transaction(self, cointag, rawhex):
        self.params.update({
                  'method': 'send_raw_transaction',
                  'coin': cointag, "tx_hex":rawhex})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    # sell base, buy rel.
    def setprice(self, base, rel, basevolume, relprice, trademax=False, cancel_previous=True):
        self.params.update({
                  'method': 'setprice',
                  'base': base,
                  'rel': rel,
                  'volume': basevolume,
                  'price': relprice,
                  'max':trademax,
                  'cancel_previous':cancel_previous})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def set_required_confirmations(self):
        pass

    def set_requires_notarization(self):
        pass

    def show_priv_key(self):
        pass

    def stop(self):
        pass

    def unban_pubkeys(self):
        pass

    def version(self):
        self.params.update({'method': 'version'})
        r = requests.post(self.node_ip, json=self.params)
        return r.json()

    def withdraw(self, cointag, address, amount):
        self.params.update({
                  'method': 'withdraw',
                  'coin': cointag,
                  'to': address,
                  'amount': amount})
        r = requests.post(self.node_ip, json=self.params)
        return r.json() 

    def withdraw_all(self, cointag, address):
        self.params.update({
                  'method': 'withdraw',
                  'coin': cointag,
                  'to': address,
                  'max': True})
        r = requests.post(self.node_ip, json=self.params)
        return r.json() 

    def list_coins(self):
        coins_list = {
            "enabled":[],
            "inactive":[]
        }
        enabled = self.get_enabled_coins_list()
        for coin in self.coins:
            if coin['coin'] in enabled:
                coins_list['enabled'].append(coin['coin'])
            else:
                coins_list['inactive'].append(coin['coin'])
        return coins_list




    '''









    def get_unfinished_swaps(self):
        unfinished_swaps = []
        unfinished_swap_uuids = []
        recent_swaps = my_recent_swaps(self, 50).json()
        for swap in recent_swaps['result']['swaps']:
            swap_events = []
            for event in swap['events']:
                swap_events.append(event['event']['type'])
            if 'Finished' not in swap_events:
                unfinished_swaps.append(swap)
                unfinished_swap_uuids.append(swap['uuid'])
        return unfinished_swap_uuids, unfinished_swaps
    '''

mm2 = mm2_proxy(coins, mm2_creds['rpc_password'], mm2_creds['node_ip'])
