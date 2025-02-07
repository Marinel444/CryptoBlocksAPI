from celery import shared_task
from .service import BlockService


@shared_task
def fetch_and_store_blocks():
    coin_market_cap = BlockService(provider_name="CoinMarketCap", currency="BTC").run()
    block_chair = BlockService(provider_name="BlockChair", currency="ETH").run()
    msg = (
        f"Task 1 : {coin_market_cap}\n"
        f"Task 2 : {block_chair}\n"
    )
    print(msg)
    return msg
