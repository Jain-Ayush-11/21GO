from django.contrib import admin
from . import models

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('day', 'id')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id')

# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Wallpaper, WallpaperAdmin)
admin.site.register(models.Relapse)
admin.site.register(models.Achievements)
admin.site.register(models.Post)
admin.site.register(models.Journal)