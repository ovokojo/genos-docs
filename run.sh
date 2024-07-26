#!/bin/bash

# Ensures the scripts in the frontend and backend directories are executable
chmod +x ./terminate.sh
chmod +x frontend/run.sh
chmod +x backend/run.sh

# Ports to be used by the frontend and backend
FRONTEND_PORT=3000
BACKEND_PORT=$(grep FLASK_APP_PORT backend/.env | cut -d '=' -f2)

# Terminate any processes using the frontend and backend ports
if [ -f "./terminate.sh" ]; then
    echo "Terminating ports..."
    source ./terminate.sh
    terminate $FRONTEND_PORT
    terminate $BACKEND_PORT
else
    echo "terminate.sh not found!"
    exit 1
fi

# Function to run the backend Flask app
run_backend() {
    echo "Starting Flask app..."
    cd backend
    ./run.sh &
    cd ..
}

# Function to run the frontend Flutter app
run_frontend() {
    echo "Starting Flutter app..."
    cd frontend
    ./run.sh &
}

# Run backend first, then frontend
run_backend
run_frontend

# Wait for all background processes to finish
wait
