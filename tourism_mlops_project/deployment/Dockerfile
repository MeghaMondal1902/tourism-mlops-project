# Use Python 3.9 as the base image

FROM python:3.9

# Set the working directory inside the container

WORKDIR /app

# Copy project files into the container

COPY . .

# Install all required dependencies

RUN pip install -r requirements.txt

# Create a non-root user for security

RUN useradd -m -u 1000 user

# Switch to the non-root user

USER user

# Configure environment variables

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set the working directory for the user

WORKDIR $HOME/app

# Copy application files with appropriate permissions

COPY --chown=user . $HOME/app

# Run the Streamlit application

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
