from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','food_type', 'created','rating','address')
    list_filter = ('created','name',)
    search_fields = ('name','description')
    ordering = ['created',]
admin.site.register(Restaurant, RestaurantAdmin)
