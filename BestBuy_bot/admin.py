from django.contrib import admin
from django.contrib import admin
from .models import User, Orders, OrderItem, Products, Categories, ChannelPosts, LoyaltyProgram, UserActivityLogs, DeliveryMethods, Promocodes, Branches, PaymentMethods, Variations, BotConfiguration, SMSCampaigns, Reviews, ExportHistory

admin.site.register(User)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(ChannelPosts)
admin.site.register(LoyaltyProgram)
admin.site.register(UserActivityLogs)
admin.site.register(DeliveryMethods)
admin.site.register(Promocodes)
admin.site.register(Branches)
admin.site.register(PaymentMethods)
admin.site.register(Variations)
admin.site.register(BotConfiguration)
admin.site.register(SMSCampaigns)
admin.site.register(Reviews)
admin.site.register(ExportHistory)
# Register your models here.
