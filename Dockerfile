FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Train model inside container
RUN python train_model.py

# Run API 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
