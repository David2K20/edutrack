#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process for Render..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Verify Django is installed and working
echo "Verifying Django installation..."
python -c "import django; print('Django version:', django.get_version())"

# Verify our project structure
echo "Checking project structure..."
ls -la

# Ensure media directory exists for uploads
echo "Ensuring media directory exists..."
mkdir -p media

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Ensure admin user exists
echo "Creating/updating admin user..."
python manage.py ensure_admin_user

echo "Build completed successfully for Render!"
