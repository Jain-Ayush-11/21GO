from django.contrib import admin
from . import models

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('day', 'id')

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Wallpaper, WallpaperAdmin)