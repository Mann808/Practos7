from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'


from django.apps import AppConfig

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self):
        import sys
        if 'manage.py' in sys.argv[0]:
            from .models import Role
            roles = ['buyer', 'seller', 'admin', 'warehouse_manager', 'support']
            
            try:
                for role_name in roles:
                    Role.objects.get_or_create(role_name=role_name)
            except Exception as e:
                print(f"Error creating roles: {e}")