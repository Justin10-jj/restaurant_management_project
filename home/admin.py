from django.contrib import admin

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','address','phone_number','email')
    search_field=('name','address')
    list_filter=('is_active',)