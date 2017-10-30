# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Crop,Warehouse,Market,market_crop_price,Transportation

admin.site.register(Crop)
admin.site.register(Warehouse)
admin.site.register(Market)
admin.site.register(Transportation)
admin.site.register(market_crop_price)

