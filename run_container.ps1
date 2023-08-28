# Define variables
$CONTAINER_NAME = "rapid-container"
$PORT_MAPPING = "8080:80"

# Run the Docker container
docker run -d --name $CONTAINER_NAME -p $PORT_MAPPING rapid-app