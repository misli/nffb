from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import BackgroundExtension

class BackgroundExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(BackgroundExtension, BackgroundExtensionAdmin)
