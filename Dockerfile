# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy API files
COPY . .

# Expose API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
