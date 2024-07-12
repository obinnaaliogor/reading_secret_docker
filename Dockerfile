FROM python:3.9-slim

# Copy the Python script
COPY app.py /app/app.py

# Set the working directory
WORKDIR /app

# Ensure secrets directory exists
# RUN mkdir -p /run/secrets

# Run the Python script
CMD ["python", "app.py"]
