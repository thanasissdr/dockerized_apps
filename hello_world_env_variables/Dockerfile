ARG PYTHON_VERSION=3.10.4
FROM python:${PYTHON_VERSION}-slim

# Make the following the working directory inside the container
WORKDIR /dst 

# Copy the contents of the source folder "src" into "/dst"
COPY src ${WORKDIR}

# Define environment variables that can be accessible
# within our application
ENV USERNAME=BOB
ENV RANDOM_VARIABLE=10000000

ENTRYPOINT ["python", "main.py"]
