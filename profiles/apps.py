from django.apps import AppConfig
from django.core.signals import request_finished


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    verbose_name = 'Профили'

    def ready(self):
        from profiles import signals  # noqa
        # request_finished.connect(signals.create_profile)
