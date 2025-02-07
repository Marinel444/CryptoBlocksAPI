from django.contrib import admin
from .models import Currency, Provider, Block


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "symbol"]
    search_fields = ("name", "symbol")


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "url", "api_key"]
    search_fields = ("name", "api_key")


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ["id", "get_currency_symbol", "get_provider_name", "block_number", "created_at"]
    search_fields = ("currency__symbol", "provider__name")

    def get_currency_symbol(self, obj):
        return obj.currency.symbol

    get_currency_symbol.short_description = "Currency"

    def get_provider_name(self, obj):
        return obj.provider.name

    get_provider_name.short_description = "Provider"
