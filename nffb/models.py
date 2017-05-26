import re

from django import forms
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField


class ColorInput(forms.TextInput):
    input_type = 'color'


class ColorField(models.CharField):
    default_validators = [RegexValidator(
        re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'),
        _('Enter a valid hex color.'),
        'invalid',
    )]
 
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)
 
    def formfield(self, **kwargs):
        kwargs['widget'] = ColorInput
        return super(ColorField, self).formfield(**kwargs)
 

@extension_pool.register
class BackgroundExtension(PageExtension):
    image = FilerImageField(verbose_name=_('background image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    position = models.CharField(_('background position'), default='center center', max_length=15)
    color = ColorField(_('background color'), default='#ffffff')
