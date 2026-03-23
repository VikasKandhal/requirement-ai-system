FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use Render's dynamic port
ENV PORT=10000

EXPOSE 10000

# Health check using dynamic port
HEALTHCHECK CMD curl --fail http://localhost:$PORT/health || exit 1

# Start FastAPI properly
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
