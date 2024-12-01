import os
from django.contrib.auth import get_user_model # type: ignore

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seguridad.settings")

import django # type: ignore
django.setup()

User = get_user_model()

# Verificar si existe un superusuario, si no, lo crea.
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
    print("Superusuario creado exitosamente")
else:
    print("El superusuario ya existe")
