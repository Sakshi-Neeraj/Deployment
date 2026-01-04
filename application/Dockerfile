# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Use gunicorn for production-grade server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]