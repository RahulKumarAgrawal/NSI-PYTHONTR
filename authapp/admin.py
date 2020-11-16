from django.contrib import admin
from .models import User
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import render
# from django.contrib.auth.admin import UserAdmin

class UserModelAdmin(admin.ModelAdmin):
	list_display = ["email","url_field","username","phone","first_name","last_name","groups"]
	list_display_links = ["email","url_field"]
	list_editable = ["username","phone","first_name","last_name","groups"]
	list_filter =["username"]
	actions = ['detail_page']
	def detail_page(self,request,queryset):
		return render(request, 'admin/custom_template.html', context={})
	detail_page.short_description = "users detail page"
	# def get_urls(self):
	# 	urls = super().get_urls()
	# 	custom_urls = [
	# 		url(r'^(?P<account_id>.+)/deposit/$',
    #             self.admin_site.admin_view(self.process_deposit),
    #             name='account-deposit',)
	# 	]
	# 	return custom_urls+urls

	# def account_actions(self, obj):
	# 	return format_html(
	# 		'<a class="button" href="{}">Detail</a>',
	# 		reverse('admin:user-detail', args[obj.pk]),
	# 	)
	# 	account_actions.short_description = 'Account Actions'
	# 	account_actions.allow_tags = True

	class Meta:
		model = User

admin.site.register(User,UserModelAdmin)

# class CustomUserAdmin(UserAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()  # type: Set[str]

#         if not is_superuser:
#             disabled_fields |= {
#                 'username',
#                 'is_superuser',
#                 'user_permissions',
#             }

#         for f in disabled_fields:
#             if f in form.base_fields:
#                 form.base_fields[f].disabled = True

#         return form