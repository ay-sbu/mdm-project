# Tests

> main tests are in the `api.tests.py`.
> these are just some debug and unstandard tests.

## server-app

### curl

- add user

```shell
curl -X POST -H 'Content-Type: application/json' -d '{"username": "alialavi", "password": "aA1234%^"}' -i http://127.0.0.1:8000/auth/users/
```

- create refresh and access tokens:

```shell
curl -X POST -H 'Content-Type: application/json'  -d '{"username": "alialavi", "password": "aA1234%^"}'  http://127.0.0.1:8000/auth/jwt/create
```

- get devices

```shell
curl -X GET -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -i http://127.0.0.1:8000/api/v1/devices/
```

- add new device

```shell
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d '{"device_name": "Galaxy M12", "device_type": "Android", "os_version": "12.0"}' -i http://127.0.0.1:8000/api/v1/devices/
```

### ws

- installation

```shell
pip install websockets-cli
```

- connect to websocket

```shell
ws listen ws://localhost:8000/ws/
```
