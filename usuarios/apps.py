from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'  # Asegúrate de que este sea el nombre correcto de tu app

    def ready(self):
        import usuarios.signals  # Aquí registras las señales