from django.contrib import admin
from . import models

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('day', 'id')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id')

# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Wallpaper, WallpaperAdmin)