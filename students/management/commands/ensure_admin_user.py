"""
Django management command to ensure admin user exists with credentials from environment variables.
This command creates or updates the admin user using secure environment variables.
"""

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Ensures admin user exists with credentials from environment variables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            help='Admin username (overrides DJANGO_ADMIN_USERNAME env var)',
        )
        parser.add_argument(
            '--email',
            type=str,
            help='Admin email (overrides DJANGO_ADMIN_EMAIL env var)',
        )
        parser.add_argument(
            '--password',
            type=str,
            help='Admin password (overrides DJANGO_ADMIN_PASSWORD env var)',
        )

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from command line args or environment variables
        username = options['username'] or os.environ.get('DJANGO_ADMIN_USERNAME', 'admin')
        email = options['email'] or os.environ.get('DJANGO_ADMIN_EMAIL', 'admin@example.com')
        password = options['password'] or os.environ.get('DJANGO_ADMIN_PASSWORD')
        
        if not password:
            self.stdout.write(
                self.style.ERROR(
                    'Admin password not provided. Set DJANGO_ADMIN_PASSWORD environment variable '
                    'or use --password argument.'
                )
            )
            return
        
        # Get or create the admin user
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
            }
        )
        
        # Update user properties (in case user already existed but needs updates)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created admin user: {username}')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully updated admin user: {username}')
            )
        
        # Verify the user can authenticate (optional security check)
        from django.contrib.auth import authenticate
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            self.stdout.write(
                self.style.SUCCESS('✓ Admin user authentication verified')
            )
        else:
            self.stdout.write(
                self.style.WARNING('⚠ Admin user authentication failed - please check credentials')
            )
