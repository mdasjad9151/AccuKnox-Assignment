from django.apps import AppConfig


class Question1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question1'


        # Importing signals
    def ready(self):
        import question1.signals