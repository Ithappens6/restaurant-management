# Docker Setup Guide

This guide explains how to run the Restaurant Backend API using Docker.

## 📋 Prerequisites

- Docker installed on your system
- Docker Compose (optional, but recommended)

## 🔧 Environment Variables

The application uses Pydantic Settings to manage configuration. Environment variables can be set in three ways:

### 1. Using `.env` file (Recommended for local development)

Create a `.env` file in the backend directory:

```bash
# Copy the example file
cp env.example .env

# Edit with your actual values
nano .env
```

Required environment variables:
- `OPENAI_API_KEY` - Your OpenAI API key
- `SENDGRID_API_KEY` - Your SendGrid API key (for email notifications)

Optional environment variables (have defaults in `app/core/config.py`):
- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 8000)
- `DEBUG` - Debug mode (default: true)
- `DATABASE_URL` - Database connection string
- `RESTAURANT_NAME`, `RESTAURANT_ADDRESS`, `RESTAURANT_PHONE` - Restaurant info
- `SENDGRID_FROM_EMAIL`, `SENDGRID_FROM_NAME` - Email sender info

### 2. Using Docker Environment Variables

Pass environment variables directly when running the container:

```bash
docker run -e OPENAI_API_KEY=your_key -e SENDGRID_API_KEY=your_key -p 8000:8000 restaurant-backend
```

### 3. Using docker-compose.yml (Recommended for production)

The provided `docker-compose.yml` file is already configured to read from your environment or `.env` file.

## 🚀 Quick Start

### Option 1: Using Docker Compose (Easiest)

```bash
# 1. Create .env file with your secrets
cp env.example .env
# Edit .env with your actual API keys

# 2. Build and run
docker-compose up -d

# 3. View logs
docker-compose logs -f

# 4. Stop the container
docker-compose down
```

### Option 2: Using Docker directly

```bash
# 1. Build the image
docker build -t restaurant-backend .

# 2. Run the container
docker run -d \
  --name restaurant-backend \
  -p 8000:8000 \
  -e OPENAI_API_KEY=your_openai_key \
  -e SENDGRID_API_KEY=your_sendgrid_key \
  -v $(pwd)/data:/app/data \
  restaurant-backend

# 3. View logs
docker logs -f restaurant-backend

# 4. Stop the container
docker stop restaurant-backend
docker rm restaurant-backend
```

## 📊 Accessing the Application

Once running, access:
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **Root**: http://localhost:8000/

## 💾 Database Persistence

The SQLite database is stored in the `/app/data` directory inside the container. To persist data:

1. **Using docker-compose**: Already configured with volume mount to `./data`
2. **Using docker run**: Add `-v $(pwd)/data:/app/data` to mount local directory

## 🔍 Troubleshooting

### Check if container is running
```bash
docker ps
```

### View logs
```bash
docker-compose logs -f backend
# OR
docker logs -f restaurant-backend
```

### Access container shell
```bash
docker exec -it restaurant-backend /bin/bash
```

### Rebuild after code changes
```bash
docker-compose up -d --build
```

## 🛠️ Development vs Production

### Development
- Set `DEBUG=true`
- Use SQLite database
- Mount code as volume for hot reload (not included by default):
  ```yaml
  volumes:
    - ./app:/app/app
  ```

### Production
- Set `DEBUG=false`
- Use production-grade database (PostgreSQL, MySQL)
- Don't mount code as volume
- Set appropriate `CORS_ORIGINS`
- Use secrets management (Docker secrets, Kubernetes secrets, etc.)

## 🔐 Security Notes

1. **Never commit** `.env` files with real secrets
2. **Use** environment variables or secrets management in production
3. **Update** `CORS_ORIGINS` to restrict allowed origins in production
4. **Consider** using a proper database (PostgreSQL) instead of SQLite for production

## 📝 Example Production Deployment

For production, consider using environment variables instead of `.env` file:

```yaml
version: '3.8'
services:
  backend:
    image: restaurant-backend:latest
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}  # Read from system env
      - SENDGRID_API_KEY=${SENDGRID_API_KEY}
      - DEBUG=false
      - DATABASE_URL=postgresql://user:pass@db:5432/restaurant
    depends_on:
      - db
  
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=restaurant
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

