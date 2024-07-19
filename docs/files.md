# File Upload and Download API Documentation

This API provides endpoints to upload, list, and download files using Flask.

## Endpoints

| Endpoint                  | Method | Description                             |
|---------------------------|--------|-----------------------------------------|
| `/file/`                  | GET    | Retrieves a list of all uploaded files. |
| `/file/<int:id>`          | GET    | Retrieves details of a file by its ID.  |
| `/file/upload`            | POST   | Uploads a new file to the server.       |
| `/file/download/<int:id>` | GET    | Downloads a file by its ID.             |
| `/file/delete/<int:id>`   | DELETE | Deletes a file by its ID.               |

## Example Usage

### Uploading a File

```bash
curl -X POST -F 'file=@/path/to/your/file.txt' http://your-api-url/file/upload
```

### Downloading a File

```bash
curl -X GET http://your-api-url/file/download/1 -o downloaded_file.txt
```

### Deleting a File

```bash
curl -X DELETE http://your-api-url/file/delete/1
```

Replace `http://your-api-url` with the actual base URL of your API server.

## Request Parameters

### Upload File Endpoint

| Parameter | Type                | Required | Description         |
|-----------|---------------------|----------|---------------------|
| `file`    | multipart/form-data | Yes      | The file to upload. |

## Response Examples

### Successful Upload Response

```json
{
  "id": 1,
  "filename": "example.txt",
  "filepath": "/path/to/uploaded/files/example.txt"
}
```

### Error Responses

| HTTP Status Code | Response Body                        | Reason                                       |
|------------------|--------------------------------------|----------------------------------------------|
| 400              | `{"error": "No file part"}`          | No file part provided in the upload request. |
| 400              | `{"error": "No selected file"}`      | Empty file upload request.                   |
| 400              | `{"error": "File type not allowed"}` | Uploaded file has an unsupported file type.  |
| 404              | `{"error": "File not found"}`        | File requested for download does not exist.  |

