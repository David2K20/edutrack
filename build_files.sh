#!/bin/bash

# Build script for Vercel deployment
echo "Starting Vercel build..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Copy static files to build directory
echo "Copying static files for Vercel..."
mkdir -p staticfiles_build
cp -r staticfiles/* staticfiles_build/

echo "Build completed successfully!"
