FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the Flask app files to the container
COPY entrypoint.sh app.py requirements.txt index.html ./

# Set timezone to Budapest
RUN apk add --no-cache tzdata
RUN ln -sf /usr/share/zoneinfo/Europe/Budapest /etc/localtime

# Install flask
RUN pip install --no-cache-dir -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose port 5000 for web traffic
EXPOSE 5000

# Set the entrypoint script to start the Flask app
ENTRYPOINT ["./entrypoint.sh"]
