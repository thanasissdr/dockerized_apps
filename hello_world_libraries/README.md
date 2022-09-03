# INSTRUCTIONS

## 2 steps
### Build the image
#### Using default value for python version (3.10.4)

```cmd
docker build --file Dockerfile --tag hello_world:libraries .
```
#### Using a build argument to change the python version (3.9.5)
```cmd
docker build --file Dockerfile --tag hello_world:libraries --build-arg PYTHON_VERSION=3.9.5 .
```
#### Using a python version such that the requirements are not met (3.6.9)
```cmd
docker build --file Dockerfile --tag hello_world:libraries --build-arg PYTHON_VERSION=3.6.9 .
```

### Run the application (while creating the container)
```cmd
docker run hello_world:libraries
```


## Using `docker-compose`

```cmd
docker compose --file docker-compose-hello_world_libraries.yml up
```