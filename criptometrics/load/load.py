from tinydb import TinyDB
from criptometrics.extract import extract
from criptometrics.transform import transform


def load(updated_data):
    btc_coinbase_api = TinyDB('criptometrics/utils/btc_coinbase_api.json')
    btc_coinbase_api.insert(updated_data)
