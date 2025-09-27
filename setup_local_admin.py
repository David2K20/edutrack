#!/usr/bin/env python
"""
Local script to set up admin user for testing before deployment.
This script creates an admin user locally so you can test the system.
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to the Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# Initialize Django
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

def create_local_admin():
    """Create a local admin user for testing"""
    User = get_user_model()
    
    username = 'admin'
    email = 'admin@edutrack.com'
    password = 'admin123'  # Simple password for local testing
    
    # Remove existing admin user if exists
    if User.objects.filter(username=username).exists():
        User.objects.filter(username=username).delete()
        print(f"Removed existing user: {username}")
    
    # Create new admin user
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    
    print(f"✅ Created local admin user:")
    print(f"   Username: {username}")
    print(f"   Email: {email}")
    print(f"   Password: {password}")
    print(f"")
    print(f"🚀 You can now run 'python manage.py runserver' and login at /admin/")
    print(f"")
    print(f"📝 Note: This is for LOCAL TESTING ONLY.")
    print(f"   For production on Render, the admin credentials are set via environment variables.")

if __name__ == '__main__':
    # Run migrations first
    print("Running migrations...")
    call_command('migrate')
    
    # Create admin user
    create_local_admin()
