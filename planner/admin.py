from django.contrib import admin

from .models import Guests, Finance, Buffet
# Register your models here.

admin.site.register(Guests)
admin.site.register(Finance)
admin.site.register(Buffet)
