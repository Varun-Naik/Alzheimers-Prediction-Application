# Create a Dockerfile that specifies the environment needed to run
# the FastAPI app, including dependencies and packages.


FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the port
EXPOSE 80

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
