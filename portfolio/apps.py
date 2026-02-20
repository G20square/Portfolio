from django.apps import AppConfig

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'

    def ready(self):
        from django.contrib.auth.models import User
        field = User._meta.get_field('username')
        # Remove all validators including default ones
        field.validators = []
        field.default_validators = []
