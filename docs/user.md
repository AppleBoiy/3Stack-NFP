# User API Documentation

This API provides endpoints to manage users, including registration, login, and retrieving user information using Flask.

## Endpoints

| Endpoint          | Method | Description                                         |
|-------------------|--------|-----------------------------------------------------|
| `/users/`         | GET    | Retrieves a list of all users.                      |
| `/users/register` | POST   | Registers a new user.                               |
| `/users/login`    | POST   | Logs in a user and returns a JWT.                   |
| `/users/logout`   | POST   | Logs out the current user.                          |
| `/users/whoami`   | GET    | Retrieves the current logged-in user's information. |

## Example Usage

### Listing all Users

```bash
curl -X GET http://your-api-url/users/
```

### Registering a New User

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "newuser", "password": "password"}' http://your-api-url/users/register
```

### Logging in a User

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "newuser", "password": "password"}' http://your-api-url/users/login
```

### Logging out a User

```bash
curl -X POST -H "Authorization: Bearer <access_token>" http://your-api-url/users/logout
```

### Retrieving Current User Info

```bash
curl -X GET -H "Authorization: Bearer <access_token>" http://your-api-url/users/whoami
```

Replace `http://your-api-url` with the actual base URL of your API server and `<access_token>` with the JWT received
from the login endpoint.

## Request/Response Examples

### Request Body (Register and Login)

```json
{
  "username": "newuser",
  "password": "password"
}
```

### Response Examples

#### Successful Registration Response

```json
{
  "message": "User <username:newuser> created successfully"
}
```

#### Error Response (User Already Exists)

```json
{
  "message": "User <username:newuser> already exists"
}
```

#### Successful Login Response

```json
{
  "access_token": "<jwt_token>"
}
```

#### Successful Logout Response

```json
{
  "message": "Successfully logged out"
}
```

#### Error Response (Invalid Credentials)

```json
{
  "message": "Invalid credentials"
}
```

#### Successful Response (WhoAmI)

```json
{
  "id": 1,
  "username": "newuser"
}
```

## Error Responses

| HTTP Status Code | Response Body                                           | Reason                                          |
|------------------|---------------------------------------------------------|-------------------------------------------------|
| 400              | `{"message": "User <username:newuser> already exists"}` | Attempting to register an existing user.        |
| 401              | `{"message": "Invalid credentials"}`                    | Incorrect username or password during login.    |
| 404              | `{"message": "User not found"}`                         | User does not exist (when applicable).          |
| 401              | `{"message": "Missing Authorization Header"}`           | Authorization header is missing in the request. |

### Logout Endpoint

#### `/users/logout` - POST

Logs out the current user.

No request body is required. The endpoint expects an `Authorization` header with the format `Bearer <access_token>`.

Returns a success message upon successful logout.

