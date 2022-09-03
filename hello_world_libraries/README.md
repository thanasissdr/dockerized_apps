# INSTRUCTIONS

## 2 steps
### Build the image
```cmd
docker build --file Dockerfile --tag hello_world:libraries --build-arg PYTHON_VERSION=3.10.4 .
```

### Run the application (while creating the container)
```cmd
docker run hello_world:libraries
```


## Using `docker-compose`

```cmd
docker compose --file docker-compose-hello_world_libraries.yml up
```