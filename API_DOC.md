# File Info API Documentation

Welcome to the File Info API documentation. This API allows you to upload files and retrieve information about them.

## Endpoints

### Upload a File

Upload a file to the server.

- **Endpoint:** `POST /upload`
- **Description:** Uploads a file to the server.
- **Request:**
  - Method: POST
  - Headers: `Content-Type: multipart/form-data`
  - Body: File attachment
- **Response:**
  - JSON object with a `message` field indicating the success or error

#### Example Request

```bash
curl -X POST -F "file=@path/to/file.txt" http://yourserver/upload

Example Response: 
    {
    "message": "File uploaded successfully"
    }

Get File Information:
    -Retrieve information about an uploaded file.

Endpoint: POST /get_file_info
Description: Retrieves information about an uploaded file.
Request:
Method: POST
Headers: Content-Type: multipart/form-data
Body: File attachment
Response:
JSON object containing file information
Example Request
bash
Copy code
curl -X POST -F "file=@path/to/file.txt" http://yourserver/get_file_info
Example Response
json
Copy code
{
  "file_type": "ASCII text",
  "file_name": "file.txt",
  "file_size": "12345 bytes"
}
HTTP Methods: POST vs. GET
We use the POST method for both uploading files and retrieving file information to adhere to REST principles. The POST method is used for creating resources, which aligns with uploading a file. It's also used for retrieving information when the request has a complex payload, as is the case here.

For more simple read-only operations, GET could be used. However, to keep consistency and adhere to best practices, we use POST for both operations.

Conclusion
Thank you for using the File Info API. If you have any questions or feedback, please don't hesitate to contact us.
