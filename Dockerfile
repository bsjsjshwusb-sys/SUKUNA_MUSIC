FROM nikolaik/python-nodejs:python3.10-nodejs20

# Install FFmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Copy repository
COPY . .

# Install dependencies
RUN python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir -r requirements.txt

# Start SUKUNA MUSIC
CMD ["python3", "-m", "SHUKLAMUSIC"]
