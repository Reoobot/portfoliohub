#!/bin/bash

# Esperar a que la base de datos esté lista
echo "⏳ Esperando a que MySQL esté disponible..."
until nc -z db 3306; do
  sleep 1
done
echo "✅ MySQL está disponible."

# Aplicar migraciones
echo "📦 Aplicando migraciones..."
python manage.py migrate

# Crear usuario vulnerable si no existe
echo "👤 Verificando usuario vulnerable..."
python manage.py shell <<EOF
from accounts.models import VulnerableUser
if not VulnerableUser.objects.filter(username='Hacker').exists():
    VulnerableUser.objects.create(username='Hacker', password='admin123')
    print("✅ Usuario vulnerable creado.")
else:
    print("ℹ️ Usuario vulnerable ya existe.")
EOF

# Iniciar el servidor
echo "🚀 Iniciando servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
