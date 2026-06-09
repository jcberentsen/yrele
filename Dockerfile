FROM python:3.14-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the internal port
EXPOSE 8000

# Run Uvicorn pointing to your file (main.py) and app object (app)
CMD ["uvicorn", "src.server.app:app", "--host", "0.0.0.0", "--port", "1876"]
