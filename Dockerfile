# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install uvicorn separately to ensure it's installed
RUN pip install --no-cache-dir uvicorn

# Copy the project files into the container
COPY . .

# Expose the FastAPI app port
EXPOSE 8000

# Set the entry point for the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
