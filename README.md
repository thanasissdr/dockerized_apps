# GENERAL

The following folders contain examples on how to dockerize our application.

Steps to take:

1. Look at the `src` folder to see what the main application does.
2. Build a docker image (take a look at the steps in the corresponding `Dockerfile`)
> We can take a look at the built images by typing
```cmd
docker image ls 
```
3. Run the image (a docker container is created)
The application should be executed.
> We can take a look at the docker containers by typing
```cmd
docker container ls -a
```


The suggested order to look at the examples is:

- hello_world
- hello_world_libraries
- hello_world_env_variables



Alternatively, we can use `docker-compose`, which simplifies the steps described above.

- volumes
- docker-compose-examples-ui