from django.apps import AppConfig


class Question3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question3'

    # Importing signals
    def ready(self):
        import question3.signals