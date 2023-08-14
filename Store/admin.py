from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ebook)
class CrispAdmin(admin.ModelAdmin):
    list_display = ('item', 'price')
admin.site.register(Crisp, CrispAdmin)

class WaffleUPAdmin(admin.ModelAdmin):
    list_display = ('item', 'price')
admin.site.register(WaffleUP, WaffleUPAdmin)