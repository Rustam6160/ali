from django.contrib import admin
from .models import NaturePlace

@admin.register(NaturePlace)
class NaturePlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    search_fields = ('title', 'location')
