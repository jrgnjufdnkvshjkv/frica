from django.contrib import admin
from .models import Computers, Categary, Man_clothes, Womans_clothes, Contact
# Register your models here.
admin.site.register(Contact)
admin.site.register(Categary)
admin.site.register(Man_clothes)
admin.site.register(Womans_clothes)

@admin.register(Computers)
class ComputersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
