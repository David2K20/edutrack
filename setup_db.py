#!/usr/bin/env python
"""
Setup script to initialize the database on first deployment
"""
import os
import sys
import django
from pathlib import Path

# Add the project directory to the path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.db import connection

def main():
    print("🚀 Setting up database for Django Student Management System...")
    
    try:
        # Test database connection
        print("📡 Testing database connection...")
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
        
        # Run migrations
        print("📋 Running database migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        print("✅ Migrations completed!")
        
        print("🎉 Database setup completed successfully!")
        print(f"🌐 Your app should now work at: https://edutrack-jq78ljzof-davids-projects-4823aa19.vercel.app")
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        return False
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
