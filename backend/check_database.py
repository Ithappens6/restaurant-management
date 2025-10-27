#!/usr/bin/env python3
"""
Database Inspector - View stored data
"""
import sqlite3
from datetime import datetime

DATABASE_PATH = "restaurant.db"

def inspect_database():
    """Inspect the SQLite database and display contents"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("🗄️  RESTAURANT DATABASE INSPECTION")
        print("=" * 70)
        
        # Check reservations
        cursor.execute("SELECT COUNT(*) FROM reservations")
        reservation_count = cursor.fetchone()[0]
        print(f"\n📅 RESERVATIONS ({reservation_count} total)")
        print("-" * 70)
        
        if reservation_count > 0:
            cursor.execute("""
                SELECT id, restaurant_id, name, email, date, time, party_size, 
                       status, created_at 
                FROM reservations 
                ORDER BY created_at DESC
            """)
            
            for row in cursor.fetchall():
                print(f"  ID: {row[0]}")
                print(f"  Restaurant: {row[1]}")
                print(f"  Customer: {row[2]} ({row[3]})")
                print(f"  Date/Time: {row[4]} at {row[5]}")
                print(f"  Party Size: {row[6]} people")
                print(f"  Status: {row[7]}")
                print(f"  Created: {row[8]}")
                print("-" * 70)
        
        # Check contact messages
        cursor.execute("SELECT COUNT(*) FROM contact_messages")
        message_count = cursor.fetchone()[0]
        print(f"\n📧 CONTACT MESSAGES ({message_count} total)")
        print("-" * 70)
        
        if message_count > 0:
            cursor.execute("""
                SELECT id, restaurant_id, name, email, subject, message, created_at
                FROM contact_messages
                ORDER BY created_at DESC
            """)
            
            for row in cursor.fetchall():
                print(f"  ID: {row[0]}")
                print(f"  Restaurant: {row[1]}")
                print(f"  From: {row[2]} ({row[3]})")
                print(f"  Subject: {row[4]}")
                print(f"  Message: {row[5][:50]}..." if len(row[5]) > 50 else f"  Message: {row[5]}")
                print(f"  Created: {row[6]}")
                print("-" * 70)
        
        # Database info
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"\n📊 DATABASE STATISTICS")
        print("-" * 70)
        print(f"  Tables: {', '.join([t[0] for t in tables])}")
        print(f"  Total Records: {reservation_count + message_count}")
        print(f"  Database Size: {conn.execute('SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()').fetchone()[0] / 1024:.2f} KB")
        print("=" * 70)
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except FileNotFoundError:
        print(f"❌ Database file not found: {DATABASE_PATH}")

if __name__ == "__main__":
    inspect_database()

