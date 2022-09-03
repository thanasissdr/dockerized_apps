# INSTRUCTIONS

```cmd
docker compose --file docker-compose-multiple-services.yml up
```

The expected output is spinning up two services/servers:
- run_server
- elastic-server(es01)

In order to access the first one, open a web browser and type `localhost:8001` and for the second one (in order to see that the elastic server is up and running) open a web browser and type `localhost:9201`