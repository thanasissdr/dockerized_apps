ARG PYTHON_VERSION=3.10.4
FROM python:${PYTHON_VERSION}-slim

# Make the following the working directory inside the container
WORKDIR /dst 

# Copy the contents of the source folder "src" into "/dst"
COPY src /dst

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo "Requirements were installed"
RUN echo "Python version used: ${PYTHON_VERSION}"


ENTRYPOINT ["python", "main.py"]