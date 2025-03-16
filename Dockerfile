# Use a Windows Server Core base image with Python 3.10
FROM python:3.10-windowsservercore-ltsc2022

# Prevent Python from writing pyc files to disk and enable stdout/stderr logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache for dependencies
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
