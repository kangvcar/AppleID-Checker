# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple some-package -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run init_create_admin.py to ensure the admin user is created
# (Remove this line if you do not want to run a script to create an admin user automatically)
# RUN python init_create_admin.py

# Run app.py when the container launches
CMD ["flask", "run"]
