from django.contrib import admin
from .models import Realtor 

# Register your models here.

class RealtorAdmin(admin.ModelAdmin): 
  list_display = ('id','name','is_mvp','phone','email')
  list_display_links = ('id','name')
  list_editable = ('is_mvp',)
  list_filter = ('name',)
  search_fields = ('name','description','phone','email','hire_date')
  list_per_page = 10


admin.site.register(Realtor, RealtorAdmin)