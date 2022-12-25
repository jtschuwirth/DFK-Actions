from functions.Contracts import getHeroSale
from functions.provider import get_account, get_provider


network = "dfk"
w3 = get_provider(network)

def BuyHero(user, heroId):
    account = get_account(user, w3)
    nonce = w3.eth.get_transaction_count(account.address)
    hero_sale_contract = getHeroSale(w3, network)
    price = hero_sale_contract.functions.getCurrentPrice(int(heroId)).call()
    tx = hero_sale_contract.functions.bid(int(heroId), int(price)).build_transaction({
        "from": account.address,
        'nonce': nonce
    })

    signed_tx = w3.eth.account.sign_transaction(tx, account.key)
    hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

user = "0x7C50D01C7Ba0EDE836bDA6daC88A952f325756e3"
BuyHero(user, "")
