from django import template
from django.utils.translation import gettext as _
register = template.Library()

@register.filter
def getattr_filter(obj, attr):
  
    try:
        return getattr(obj, attr, None)
    except AttributeError:
        return None

@register.filter
def verbose_name(instance, field_name):
    if hasattr(instance, '_meta'):
        return instance._meta.get_field(field_name).verbose_name
    return field_name  