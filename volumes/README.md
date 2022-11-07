# INSTRUCTIONS

## WRITE TO VOLUMES
This section is about dealing with volumes (we can have either named volumes or bind mounts)

```cmd
cd volumes/write_to_volume
docker compose --file docker-compose.yaml up --build
```

This will create two volumes; one internal volume in `\\wsl.localhost\docker-desktop-data\version-pack-data\community\docker\volumes` (type that in File Explorer search bar on Windows) and the other one will be created inside the project directory.

Run the command
```cmd
docker compose --file docker-compose.yaml start
```
as many times as you want. Each time this command is run, a new line will be appended in the `text.txt` file.

## READ FROM VOLUMES

```cmd
cd volumes/read_volume
docker compose --file docker-compose.yaml up --build
```
where we use an external volume which we created before (when writing to volumes)

The output will be the list of the named volume.
