FROM python:3.10.4-slim

# Make the following the working directory inside the container
# and create it if it does not exist.
WORKDIR /dst

# Copy THE CONTENTS of folder "src" into "/dst" (/dst dir will be only available in the container)
COPY src /dst

ENTRYPOINT ["python", "main.py"]