FROM python:3.10-slim
 # Use the appropriate Python base image

# Install system dependencies for SQLite (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev  # for SQLite3 support

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
