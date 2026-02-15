# 1. Use Python 3.12 Slim (Small & Fast)
FROM python:3.12-slim

# 2. Set the folder inside the container
WORKDIR /app

# 3. Copy the dependency file first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your source code
COPY src/ src/

# 6. Open the port
EXPOSE 8000

# 7. Run the API
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]