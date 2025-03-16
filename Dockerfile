# Use an official Python runtime as a base image
FROM python:3.10-slim

# Prevent Python from writing pyc files to disc and enable stdout/stderr logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache for dependencies
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
