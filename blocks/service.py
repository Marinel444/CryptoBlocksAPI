import requests
from datetime import datetime
from django.utils.timezone import make_aware
from .models import Currency, Provider, Block


class BlockService:
    def __init__(self, provider_name: str, currency: str):
        self.provider = Provider.objects.get(name=provider_name)
        self.currency = Currency.objects.get(symbol=currency.upper())

    def get_coinmarketcap_block(self) -> dict:
        values = {}
        response = requests.get(
            url=self.provider.url,
            headers={"X-CMC_PRO_API_KEY": self.provider.api_key},
            params={"symbol": self.currency.symbol},
        )
        if response.status_code == 200:
            data = response.json()
            created_at = make_aware(datetime.strptime(data.get("status").get("timestamp"), "%Y-%m-%dT%H:%M:%S.%fZ"))
            values = {
                "currency": self.currency,
                "provider": self.provider,
                "block_number": Block.objects.filter(currency=self.currency).count() + 1,
                "created_at": created_at,
            }
        return values

    def get_blockchair_block(self) -> dict:
        values = {}
        url = f"{self.provider.url}{self.currency.name}/blocks?limit=1"
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            latest_block = data["data"][0]
            block_number = latest_block.get("id")
            created_at = make_aware(datetime.strptime(latest_block.get("time"), "%Y-%m-%d %H:%M:%S"))
            values = {
                "currency": self.currency,
                "provider": self.provider,
                "block_number": block_number,
                "created_at": created_at,
            }
        return values

    @staticmethod
    def save_block(values: dict) -> str:
        block, created = Block.objects.get_or_create(**values)
        if created:
            msg = f"Created new block: {block}"
        else:
            msg = f"Such a block already exists: {block}"
        return msg

    def run(self) -> str:
        msg = "Something went wrong"
        if self.provider.name == "CoinMarketCap":
            values = self.get_coinmarketcap_block()
        else:
            values = self.get_blockchair_block()
        if values:
            msg = self.save_block(values)
        return msg
