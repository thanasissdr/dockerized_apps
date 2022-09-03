# INSTRUCTIONS

```cmd
docker compose --file docker-compose-hello_world_volumes.yaml up
```

After creating the container, do
```cmd
docker compose --file docker-compose-hello_world_volumes.yaml start
```

The expected output is that a "new_string" should be created in the test.txt file every time the latter command is executed.

