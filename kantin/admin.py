from django.contrib import admin
from .models import Item, Balance

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'image')
    list_editable = ('name', 'description', 'price', 'image')

class BalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance')
    list_editable = ('balance',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Balance, BalanceAdmin)
