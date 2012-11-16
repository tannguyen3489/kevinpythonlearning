from django.contrib import admin
from chapter4.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title'] }
	
class EntryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
