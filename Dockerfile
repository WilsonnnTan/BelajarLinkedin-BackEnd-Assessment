# Use official Python 3.13 image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy dir
COPY . .

# Expose port
EXPOSE 8000

CMD ["bash", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
