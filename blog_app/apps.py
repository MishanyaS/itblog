from django.apps import AppConfig



class BlogAppConfig(AppConfig):
    """
    Configuration class for the BlogApp application.

    Attributes:
        default_auto_field (str): The default auto field to use for models.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
