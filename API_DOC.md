# RapidFort: Campus Recruitment Drive

RapidFort is a web application designed for a campus recruitment drive. It provides a REST API-based web server that allows users to upload files and retrieve information about those files. This README outlines the features, usage, and technical details of the RapidFort project.

## Features

- **File Upload:** Users can upload files via a user-friendly interface.
- **File Information:** Users can get information about uploaded files, such as file name and size.
- **Simple UI:** The web server provides a basic web page for user interaction.
- **Docker Container:** The project includes Docker containerization for easy deployment.
- **Kubernetes Support:** Kubernetes manifest files are provided to host the web server.

## Usage

### Running the Application Locally

1. Clone the repository from GitHub.
2. Navigate to the project directory:
3. Install the required Python packages:
4. Run the Flask application:
5. Access the application in your web browser at `http://127.0.0.1:5000/`.

### Uploading a File

1. Access the main page by opening the application in a web browser.
2. Click on the "Upload File" button.
3. Select a file from your local system and click "Upload."
4. You will receive a success message upon successful file upload.

### Retrieving File Information

1. Access the main page.
2. Click on the "Get File Info" button.
3. Select a file from your local system and click "Get Info."
4. You will receive information about the file, including its name, size in bytes, and size in a human-readable format.

## API Documentation

### `GET /`

- Displays the main page of the application.

### `POST /upload`

- Endpoint for file upload.
- Accepts a file in the `file` parameter of the request.
- Returns JSON response with upload status.

### `POST /get_file_info`

- Endpoint for retrieving file information.
- Accepts a file in the `file` parameter of the request.
- Returns JSON response with file information.

## Technical Details

### Project Structure

- `app.py`: Main application file containing Flask routes and logic.
- `templates/`: Directory containing HTML templates for the user interface.
- `uploads/`: Directory where uploaded files are stored.
- `Dockerfile`: Docker configuration for containerization.
- `deployment.yaml` and `service.yaml`: Kubernetes manifest files for deployment.

### Dependencies

- Flask: A micro web framework for building web applications.
- Docker: Containerization platform for packaging applications and their dependencies.

## Conclusion

RapidFort simplifies the process of file uploading and retrieval, making it an ideal solution for campus recruitment drives. With a user-friendly interface, REST API endpoints, and support for Docker and Kubernetes, RapidFort streamlines the file management process for users.

For any inquiries or issues, please contact the project maintainers or submit an issue on the [GitHub repository](https://github.com/Vaibhav4911/FileChecker).
