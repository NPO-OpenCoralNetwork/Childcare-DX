from django.contrib import admin
from .models import Tag,Inquiry,Response 

admin.site.register(Inquiry)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass