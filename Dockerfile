# Use the official Python image
FROM python:3.11-slim

# Install the working directory
WORKDIR /app

# Copy the dependencies and install them
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/main.py .

# Open port 8000
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]