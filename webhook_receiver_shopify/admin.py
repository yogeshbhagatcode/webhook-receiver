from django.contrib import admin

from .models import ShopifyOrder, ShopifyOrderItem
from webhook_receiver.models import JSONWebhookData

admin.site.register(ShopifyOrder)
admin.site.register(ShopifyOrderItem)
admin.site.register(JSONWebhookData)
