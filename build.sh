#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Verify Django is installed and working
echo "Verifying Django installation..."
python -c "import django; print(f'Django version: {django.get_version()}')"

# Debug environment variables
echo "Checking environment variables..."
echo "DB_HOST: ${DB_HOST:-NOT SET}"
echo "DB_NAME: ${DB_NAME:-NOT SET}"
echo "DB_USER: ${DB_USER:-NOT SET}"
echo "DB_PASSWORD: $(if [ -n "$DB_PASSWORD" ]; then echo "SET"; else echo "NOT SET"; fi)"
echo "ALLOWED_HOSTS: ${ALLOWED_HOSTS:-NOT SET}"

# Verify our project structure
echo "Checking project structure..."
ls -la
ls -la django_project/

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running database migrations..."
python manage.py migrate

echo "Build completed successfully!"
