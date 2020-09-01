from django.apps import AppConfig


class ManagerConfig(AppConfig):
    name = 'manager'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals
