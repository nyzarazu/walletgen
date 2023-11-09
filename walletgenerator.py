import csv
from mnemonic import Mnemonic
from eth_account import Account
import pandas as pd

def generate_wallets(n):
    # create a mnemonic object
    mnemo = Mnemonic("english")

    # prepare list to hold dictionaries of wallet details
    wallet_details = []

    for i in range(n):
        # generate a new seed phrase
        seed_phrase = mnemo.generate()

        # enable the mnemonic features of the Account class
        Account.enable_unaudited_hdwallet_features()

        # create a new account from the seed phrase
        account = Account.from_mnemonic(seed_phrase)

        # append the details to our list
        wallet_details.append({
            'seed_phrase': seed_phrase,
            'address': account.address,
            'private_key': account.key.hex()
        })

    # convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(wallet_details)

    # save the dataframe to a csv file
    df.to_csv('wallets.csv', index=False)

# generate 10 wallets and save them to a csv file
generate_wallets(5)
