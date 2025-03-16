# escape=`
FROM python:3.10-windowsservercore-ltsc2022

# Switch the default shell to PowerShell
SHELL ["powershell", "-Command"]

# Prevent Python from writing pyc files to disk and enable stdout/stderr logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache for dependencies
COPY requirements.txt .

# Upgrade pip and install dependencies (using PowerShell syntax)
RUN python -m pip install --upgrade pip ; `
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
