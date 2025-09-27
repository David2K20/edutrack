#!/usr/bin/env python
"""
Simple script to run Django migrations on Vercel
"""
import os
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    django.setup()
    
    # Run migrations
    print("Running Django migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    print("Migrations completed!")
