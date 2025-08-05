class MenuAdmin(admin.ModelAdmin):
    list_display=('name','price','description')
    search_field=('name')

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer','total_amound','status','created_at')
    list_filter=('status','created_at')