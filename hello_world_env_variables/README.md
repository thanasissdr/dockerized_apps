# INSTRUCTIONS

## 2 steps
### Build the image
```cmd
docker build --file Dockerfile --tag hello_world:env_variables .
```

### Run the application (while creating the container)
```cmd
docker run hello_world:env_variables
```

> In order to access the stopped container, you can type:
```cmd
docker run -it --rm --entrypoint /bin/bash hello_world:env_variables
```


## Using `docker-compose`

### Declaring env variables directly in the yaml file
```cmd
docker compose --file docker-compose-hello_world_env_variables.yml up
```

> The environment variables defined here are of higher priority than the ones specificed in `Dockerfile`

### Declaring environments in `.env` 
```cmd
docker compose --file docker-compose-hello_world_env_variables_alternative.yml up
```

> The environment variables defined in the `.env` file are of lower priority than the ones in the host system. 


More information can be found here:
https://docs.docker.com/compose/environment-variables/