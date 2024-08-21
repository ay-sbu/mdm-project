# User Sign Up

- process
    1. user request for registration

        ```shell
        curl -X POST -H 'Content-Type: application/json' -d '{"username": "alialavi", "password": "aA1234%^"}' -i http://127.0.0.1:8000/auth/users/
        ```
