#!/bin/bash

# ========================================
# New Developer Setup Script
# ========================================
# This script sets up the backend for a new developer
# Run this after cloning the repository

set -e  # Exit on error

echo "🍛 Setting up Restaurant Backend..."
echo "===================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip --quiet
echo "✅ Pip upgraded"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt --quiet
echo "✅ Dependencies installed"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ .env file created"
        echo "⚠️  Please update .env with your OPENAI_API_KEY"
    else
        # Create basic .env
        cat > .env << 'EOF'
# Database Configuration
DATABASE_URL=sqlite:///./restaurant.db

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
EOF
        echo "✅ Basic .env file created"
        echo "⚠️  Please update .env with your OPENAI_API_KEY"
    fi
else
    echo "✅ .env file already exists"
fi
echo ""

# Run database migrations
echo "🗄️  Setting up database..."
if [ -f "restaurant.db" ]; then
    echo "⚠️  Database file already exists, skipping migration"
    echo "   If you want to reset the database, delete restaurant.db and run:"
    echo "   python migrate.py upgrade"
else
    echo "📊 Running database migrations..."
    python migrate.py upgrade
    echo "✅ Database initialized"
fi
echo ""

# Print success message
echo "===================================="
echo "✅ Setup Complete!"
echo "===================================="
echo ""
echo "Next steps:"
echo "1. Update .env file with your OPENAI_API_KEY"
echo "2. Run the backend:"
echo "   python run.py"
echo ""
echo "3. Access the API:"
echo "   http://localhost:8000/docs"
echo ""
echo "Useful commands:"
echo "  python run.py             - Start the backend server"
echo "  python migrate.py upgrade - Apply database migrations"
echo "  python migrate.py history - View migration history"
echo "  python check_database.py  - Check database contents"
echo ""
echo "📚 Documentation:"
echo "  README.md            - Project overview"
echo "  MIGRATIONS_GUIDE.md  - Database migrations guide"
echo "  DATABASE_GUIDE.md    - Database documentation"
echo "  QUICKSTART.md        - Quick start guide"
echo ""

