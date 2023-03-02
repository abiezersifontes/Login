# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and then use it to install dependencies
RUN pip install pipenv && \
    pipenv install --system --deploy

# Copy the rest of the application code to the container
COPY . /app/

# Expose port 8000 for the web server
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
