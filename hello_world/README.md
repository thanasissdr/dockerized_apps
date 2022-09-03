# INSTRUCTIONS

## 2 steps
### Build the image
```cmd
docker build --file Dockerfile --tag hello_world:simple .
```

### Run the application (while creating the container)
```cmd
docker run hello_world:simple
```

> In order to access the stopped container, you can type:
```cmd
docker run -it --rm --entrypoint /bin/bash hello_world:simple
```


## Using `docker-compose`

```cmd
docker compose --file docker-compose-hello_world_simple.yml up
```