from functions.Contracts import getHeroRent, getSummon
from functions.provider import get_account, get_provider

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'
assistingAuctionAddress = "0x8101CfFBec8E045c3FAdC3877a1D30f97d301209"
network = "dfk"
w3 = get_provider(network)


def SummonHero(user, heroId, hireId):
    account = get_account(user, w3)
    nonce = w3.eth.get_transaction_count(account.address)
    hero_rent_contract = getHeroRent(w3, network)
    summon_contract = getSummon(w3, network)
    enhancement_stone = ZERO_ADDRESS
    summonerTears = 10
    assistantTears = 10
    price = hero_rent_contract.functions.getCurrentPrice(int(hireId)).call()
    tx = summon_contract.functions.summonCrystalWithAuction(
                                                        int(heroId), 
                                                        int(hireId), 
                                                        summonerTears, 
                                                        assistantTears,
                                                        enhancement_stone,
                                                        assistingAuctionAddress,
                                                        int(price)).build_transaction({
        "from": account.address,
        'nonce': nonce
    })
    signed_tx = w3.eth.account.sign_transaction(tx, account.key)
    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

user = "0x7C50D01C7Ba0EDE836bDA6daC88A952f325756e3"
SummonHero(user, "", "")