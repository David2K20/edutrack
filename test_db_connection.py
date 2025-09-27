#!/usr/bin/env python
"""
Test script to verify Supabase database connection
Run this after setting up your Supabase project
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

def test_database_connection():
    """Test the database connection"""
    try:
        from django.db import connection
        from django.core.management.color import make_style
        
        style = make_style('ERROR')
        
        print("🔍 Testing Supabase database connection...")
        print(f"📍 Host: {connection.settings_dict.get('HOST', 'Not set')}")
        print(f"📊 Database: {connection.settings_dict.get('NAME', 'Not set')}")
        print(f"👤 User: {connection.settings_dict.get('USER', 'Not set')}")
        print(f"🔌 Port: {connection.settings_dict.get('PORT', 'Not set')}")
        
        # Test the connection
        cursor = connection.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()[0]
        
        print(f"✅ SUCCESS: Connected to PostgreSQL!")
        print(f"📋 Database version: {version}")
        
        # Test if we can create tables (optional)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS connection_test (
                id SERIAL PRIMARY KEY,
                test_message TEXT,
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        
        cursor.execute("""
            INSERT INTO connection_test (test_message) 
            VALUES ('Django connection test successful!');
        """)
        
        cursor.execute("SELECT test_message FROM connection_test ORDER BY created_at DESC LIMIT 1;")
        test_result = cursor.fetchone()[0]
        
        print(f"✅ Database write test: {test_result}")
        
        # Clean up test table
        cursor.execute("DROP TABLE IF EXISTS connection_test;")
        connection.commit()
        
        print("🎉 All database tests passed! Ready for deployment.")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Make sure your Supabase project is running")
        print("2. Check your environment variables:")
        print("   - DB_HOST should be like: db.xxxxx.supabase.co")
        print("   - DB_PASSWORD should be your Supabase password")
        print("   - DB_NAME should be: postgres")
        print("   - DB_USER should be: postgres")
        print("3. Verify SSL connection is allowed in Supabase")
        return False

if __name__ == '__main__':
    print("🚀 Supabase Connection Test")
    print("=" * 50)
    
    # Check if environment variables are set
    required_vars = ['DB_HOST', 'DB_PASSWORD']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        print(f"⚠️  Missing environment variables: {', '.join(missing_vars)}")
        print("\n💡 To test locally, set these environment variables:")
        print("   set DB_HOST=db.xxxxx.supabase.co")
        print("   set DB_PASSWORD=your_supabase_password")
        print("   python test_db_connection.py")
    else:
        test_database_connection()
