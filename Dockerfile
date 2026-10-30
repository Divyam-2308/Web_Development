# 1. Base Image with Python runtime
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependencies list first (Docker layer caching)
COPY requirements.txt .

# 4. Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Expose the port where FastAPI runs
EXPOSE 8000

# 7. Start the FastAPI server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

