# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for Poetry
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . .

# Command to run the application

# Command to run the application, using a default port if not provided
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0"]