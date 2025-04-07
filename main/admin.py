from django.contrib import admin
from .models import userpost

# Register your models here.


@admin.register(userpost)
class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
