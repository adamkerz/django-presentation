import django.apps

class AppConfig(django.apps.AppConfig):
    name='django_presentation.forms'
    label='django_presentation_forms'


from .FormPresentationItem import FormPresentationItem
from .FormPresentationBoundItem import FormPresentationBoundItem
from .Field import Field
from .Button import Button

from .FormPresentation import FormPresentation

