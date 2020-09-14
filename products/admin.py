from django.contrib import admin

# Register your models here.
from .models import Product, Category, Store
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["name","price","category","url_field","updated", "timestamp"]
	list_display_links = ["url_field","updated",]
	list_editable = ["name","price","category"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["name", "preview_text","detail_text"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category)
admin.site.register(Store)