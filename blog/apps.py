from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Configure the blog app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
