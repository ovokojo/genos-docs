# Backend

## Getting started
Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Environments
Create a `.env` environment file in the root directory of the Backend folder.
Set `FLASK_APP_PORT` in your .env file to 5005 or a different value from the frontend port.

### Running the app
The `run.sh` scripts in this directory and the root directory will handle the creation of a virtual environment, installation of dependencies, and starting the Flask server.

Make sure the run.sh script is executable by running: `chmod +x run.sh` followed by `./run.sh`.
