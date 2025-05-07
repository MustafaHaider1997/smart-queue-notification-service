# Use lightweight Python base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Load environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run the Redis listener
CMD ["python", "redis_listener.py"]
