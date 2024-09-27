# Base image
FROM python:3.10-slim-bookworm

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project code
COPY . /app/

# Create a directory for the SQLite database
RUN mkdir -p /app/db

# Expose port 8000 for Django development server
EXPOSE 8000

# Run migrations and start the Django development server
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
