# Stage 1: Base dependencies
FROM python:3.9-slim as base

# Set working directory
WORKDIR /app

# Set non-root user
RUN groupadd -r autocloudformer && useradd -r -g autocloudformer autocloudformer
USER autocloudformer

# Install dependencies
RUN pip install --upgrade pip
RUN apt update && apt install -y libgl1-mesa-glx libglib2.0-0 libsm6 libice6 libxt6 libxext6 libxrender1

# Stage 2: Python and TensorFlow
FROM base as python
RUN pip install tensorflow

# Stage 3: AWS and Google Cloud SDK
FROM python as sdk
RUN apt update && apt install -y curl unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip
RUN curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-394.0.0-linux-x86_64.tar.gz -o google-cloud-sdk.tar.gz && \
    tar -xvf google-cloud-sdk.tar.gz && \
    ./google-cloud-sdk/install.sh --disable-installation-options && \
    rm -rf google-cloud-sdk.tar.gz

# Stage 4: AutoCloudFormer
FROM sdk as autocloudformer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Health check
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD curl --fail http://localhost:8080/health || exit 1

# Expose port
EXPOSE 8080

# Command to run
CMD ["python", "app.py"]
