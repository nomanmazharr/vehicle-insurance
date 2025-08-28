# using system python 3.12
FROM python:3.12-slim-buster

# Setting upi working directory
WORKDIR /app

# Copy all the files to the directory app
COPY . /app

# Installing dependencies
RUN pip install -r requirements.txt

# Expose port to run FastAPI
EXPOSE 5000

# Command to run app
CMD ["python3", "app.py"]