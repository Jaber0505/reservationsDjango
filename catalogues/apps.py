from django.apps import AppConfig

class CatalogueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogues'

    def ready(self):
        from django.contrib.auth.models import User

        def natural_key(self):
            return (self.username,)

        User.add_to_class('natural_key', natural_key)
