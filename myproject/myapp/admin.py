from django.contrib import admin
from .models import Product


# def mark_as_in_stock(modeladmin, request, queryset):
#     queryset.update(stock_availability=True)
# mark_as_in_stock.short_description = "Mark selected products as In Stock"

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'brand_name', 'selling_price', 'stock_availability', 'created_at')
#     prepopulated_fields = {'slug': ('product_name',)} 
#     search_fields = ('product_name', 'brand_name')
#     list_filter = ('stock_availability', 'created_at')
#     list_per_page = 20


#     fieldsets = (
#         ('Basic Information', {
#             'fields': ('product_name', 'brand_name', 'selling_price', 'original_price')
#         }),
#         ('Additional Details', {
#             'classes': ('collapse',),
#             'fields': ('available_sizes', 'description', 'stock_availability', 'warranty', 'ratings', 'product_image'),
#         }),
#     )

#     readonly_fields = ('created_at', 'updated_at')
    

    # Custom Actions
    # actions = [mark_as_in_stock]


@admin.register(Product)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_availability']

    def stock_availability(self, obj):
        return "In Stock" if obj.stock > 0 else "Out of Stock"
    stock_availability.short_description = "Stock Status"
