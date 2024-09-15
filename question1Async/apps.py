from django.apps import AppConfig


class Question1AsyncConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question1Async'

    # Importing signals
    def ready(self):
        import question1Async.signals
