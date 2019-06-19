# Official Python image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages in requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

# or we can install requests using this command
#RUN pip install requests

# copy python code
COPY app.py app.py

ENTRYPOINT ["python", "app.py"]