# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app


# Clone your GitHub repository

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY .env /app/

# Expose the port the app runs on
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]