# Greeting API Documentation

This API provides endpoints to manage greetings using Flask.

## Endpoints

| Endpoint          | Method | Description                        |
|-------------------|--------|------------------------------------|
| `/greet/`         | GET    | Retrieves a list of all greetings. |
| `/greet/`         | POST   | Creates a new greeting.            |
| `/greet/<int:id>` | GET    | Retrieves a greeting by its ID.    |
| `/greet/<int:id>` | PUT    | Updates a greeting by its ID.      |
| `/greet/<int:id>` | DELETE | Deletes a greeting by its ID.      |

## Example Usage

### Listing all Greetings

```bash
curl -X GET http://your-api-url/greet/
```

### Creating a New Greeting

```bash
curl -X POST -H "Content-Type: application/json" -d '{"msg": "Hello, World!"}' http://your-api-url/greet/
```

### Getting a Greeting by ID

```bash
curl -X GET http://your-api-url/greet/1
```

### Updating a Greeting by ID

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"msg": "Updated message"}' http://your-api-url/greet/1
```

### Deleting a Greeting by ID

```bash
curl -X DELETE http://your-api-url/greet/1
```

Replace `http://your-api-url` with the actual base URL of your API server.

## Request/Response Examples

### Request Body (POST and PUT)

```json
{
  "msg": "Hello, World!"
}
```

### Response Examples

#### Successful Response (POST/PUT)

```json
{
  "id": 1,
  "msg": "Hello, World!"
}
```

#### Successful Response (GET)

```json
{
  "id": 1,
  "msg": "Hello, World!"
}
```

#### Response (DELETE)

HTTP Status Code: `204 No Content`

## Error Responses

| HTTP Status Code | Response Body                     | Reason                                                        |
|------------------|-----------------------------------|---------------------------------------------------------------|
| 404              | `{"error": "Greeting not found"}` | Attempting to retrieve/update/delete a non-existent greeting. |


