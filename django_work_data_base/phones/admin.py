from django.contrib import admin

from phones.models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'release_date', 'lte_exists', 'slug')
    list_filter = ('lte_exists', 'release_date')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
