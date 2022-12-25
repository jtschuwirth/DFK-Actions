from functions.Contracts import getCrystal
from functions.provider import get_account, get_provider

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'
network = "dfk"
w3 = get_provider(network)

def openAllCrystals(user):
    account = get_account(user, w3)
    nonce = w3.eth.get_transaction_count(account.address)
    crystal_contract = getCrystal(w3, network)

    user_crystals = crystal_contract.functions.getUserCrystals(user).call()
    for crystal in user_crystals():
        tx = crystal_contract.functions.open(crystal).build_transaction({
            "from": account.address,
            'nonce': nonce
        })
        signed_tx = w3.eth.account.sign_transaction(tx, account.key)
        w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        nonce+=1

user = "0x7C50D01C7Ba0EDE836bDA6daC88A952f325756e3"
openAllCrystals(user)