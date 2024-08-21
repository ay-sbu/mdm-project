# JWT Authentication

1. create refresh and access tokens:

    ```shell
    curl -X POST -i -H 'Content-Type: application/json'  -d '{"username": "alialavi", "password": "aA1234%^"}'  http://127.0.0.1:8000/auth/jwt/create
    ```

2. you can get new access token:

    ```shell
    curl -X POST -i -H 'Content-Type: application/json'  -d '{"refresh": "REFRESH_TOKEN"}'  http://127.0.0.1:8000/auth/jwt/refresh
    ```

3. verify jwt token

    ```shell
    curl -X POST -i -H 'Content-Type: application/json'  -d '{"token": "REFRESH_OR_ACCESS_TOKEN"}'  http://127.0.0.1:8000/auth/jwt/refresh
    ```
