from django.contrib import admin

from home.models import Detail

# Register your models here.
# admin.site.register(Detail)
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'email','pic']