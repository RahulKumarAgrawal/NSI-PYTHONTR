from django.contrib import admin
from django.shortcuts import render
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

class StoreModelAdmin(admin.ModelAdmin):
	actions = ['download_csv']
	list_display = ["user","name","id","product"]
	list_display_links = ["user",]
	list_editable = ["name","product"]
	list_filter = ["user"]
	def download_csv(self, request, queryset):
		import csv
		from django.http import HttpResponse
		f = open('store.csv', 'w')
		writer = csv.writer(f)
		writer.writerow(["user","storename","storeid","product"])
		for s in queryset:
			writer.writerow([s.user, s.name, s.id, s.product])
		f.close()
		f = open('store.csv', 'r')
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
		return response
	download_csv.short_description = "Download CSV file for selected stats."
	class Meta:
		model = Store

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category)
admin.site.register(Store, StoreModelAdmin)