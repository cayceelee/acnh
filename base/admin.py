from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'section_type', 'display']
    fields = (
        ('title', 'display'),
        'body',
        'section_type',
        ('image_1', 'image_2'),
        'order'
    )


