from django.apps import AppConfig


class SmartzyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartzyapp'

    def ready(self):
    	import smartzyapp.signals
