#!/usr/bin/env python3
"""
Database Migration Helper Script

Usage:
    python migrate.py upgrade     # Apply all pending migrations
    python migrate.py downgrade   # Rollback one migration
    python migrate.py current     # Show current migration
    python migrate.py history     # Show migration history
    python migrate.py create "migration message"  # Create new migration
"""
import sys
import subprocess
import os

def run_alembic(command: list):
    """Run alembic command"""
    # Activate virtual environment if exists
    venv_python = os.path.join('venv', 'bin', 'python')
    if os.path.exists(venv_python):
        alembic_cmd = [venv_python, '-m', 'alembic'] + command
    else:
        alembic_cmd = ['alembic'] + command
    
    result = subprocess.run(alembic_cmd, capture_output=False)
    return result.returncode

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    action = sys.argv[1].lower()
    
    if action == 'upgrade':
        print("📈 Applying migrations...")
        return run_alembic(['upgrade', 'head'])
    
    elif action == 'downgrade':
        print("📉 Rolling back migration...")
        return run_alembic(['downgrade', '-1'])
    
    elif action == 'current':
        print("📍 Current migration:")
        return run_alembic(['current'])
    
    elif action == 'history':
        print("📜 Migration history:")
        return run_alembic(['history', '--verbose'])
    
    elif action == 'create':
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a migration message")
            print("Usage: python migrate.py create \"Add new column\"")
            sys.exit(1)
        message = sys.argv[2]
        print(f"📝 Creating new migration: {message}")
        return run_alembic(['revision', '--autogenerate', '-m', message])
    
    elif action == 'stamp':
        # Mark database as being at a specific revision without running migrations
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a revision")
            print("Usage: python migrate.py stamp head")
            sys.exit(1)
        revision = sys.argv[2]
        print(f"🔖 Stamping database at revision: {revision}")
        return run_alembic(['stamp', revision])
    
    else:
        print(f"❌ Unknown action: {action}")
        print(__doc__)
        sys.exit(1)

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)

