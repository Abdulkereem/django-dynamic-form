from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Forms)
admin.site.register(models.FormStore)
admin.site.register(models.MainForm)
admin.site.register(models.SelectOptions)
admin.site.register(models.States)