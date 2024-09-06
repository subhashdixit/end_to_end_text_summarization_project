# Use the official Python 3.10 slim-buster image as the base image
FROM python:3.10-slim-buster

# Update the package list and install AWS CLI
RUN apt update -y && apt install awscli -y

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory's contents into the /app directory in the container
COPY . /app

# Install the Python packages listed in requirements.txt
RUN pip install -r requirements.txt

# Upgrade the 'accelerate' package to the latest version
RUN pip install --upgrade accelerate

# Uninstall 'transformers' and 'accelerate' packages if they are already installed
RUN pip uninstall -y transformers accelerate

# Reinstall the 'transformers' and 'accelerate' packages
RUN pip install transformers accelerate

# Define the command to run the application
CMD ["python3", "app.py"]
