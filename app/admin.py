from django.contrib import admin
from app.models import Contact, Product

# Register your models here.


# @admin.register(Contact)
# class CustemerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'email', 'phone', 'desc', 'date']


# @admin.register(Product)
# class CustemerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'p_tag', 'catagory', 'graphycs_card', 'selling_price', 'brand', 'series', 'colors', 'item_hight', 'item_width', 'sreen_size', 'resolution',
#     'proccessor_brand', 'proccessor_type', 'proccessor_speed', 'ram_size', 'memory_technology', 'maximum_memory', 'hard_drive', 'descounted_price', 'availability', 'amazon','img1', 'img2','img3','img4','pro_bgimg01','pro_bgimg02']


admin.site.register(Contact)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)