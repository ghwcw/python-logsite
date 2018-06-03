from django.contrib import admin
from ..login import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    empty_value_display = '-NULL-'


class ConfirmStringAdmin(admin.ModelAdmin):
    empty_value_display = '-NULL-'


admin.site.register(models.User, UserAdmin)
admin.site.register(models.ConfirmString, ConfirmStringAdmin)
