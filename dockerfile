# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Set environment variables for Gunicorn
ENV GUNICORN_CMD="gunicorn --bind 0.0.0.0:$PORT --workers 3 wsgi:app"

# Expose the port the app runs on
EXPOSE $PORT

# Run the application
CMD $GUNICORN_CMD

# Define a volume for persistent storage
VOLUME ["/app/data"]
