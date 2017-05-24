from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField


@extension_pool.register
class BackgroundExtension(PageExtension):
    image = FilerImageField(verbose_name=_('background image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    position = models.CharField(_('background position'), default='center center', max_length=15)
