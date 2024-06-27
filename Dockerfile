# Use an official Python 3.12 runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV POETRY_VERSION=1.3.1

# Install Poetry
RUN python -m pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install 

# Copy the rest of the application code to the working directory
COPY . /app

# Expose port 80
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
