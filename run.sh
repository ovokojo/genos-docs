#!/bin/bash

# Ports to be used by the frontend and backend
FRONTEND_PORT=3000
BACKEND_PORT=$(grep FLASK_APP_PORT backend/.env | cut -d '=' -f2)

# Function to terminate processes running on specified ports
kill_port() {
    local PORT=$1
    local PID=$(lsof -ti:$PORT)

    if [ ! -z "$PID" ]; then
        echo "Terminating process $PID on port $PORT"
        kill -9 $PID
    fi
}

# Terminate any processes using the frontend and backend ports
kill_port $FRONTEND_PORT
kill_port $BACKEND_PORT

# Ensure sthe run.sh scripts in the frontend and backend directories are executable
chmod +x Frontend/app/run.sh
chmod +x Backend/run.sh

# Function to run the backend Flask app
run_backend() {
    echo "Starting Flask app..."
    cd Backend
    ./run.sh &
    cd ..
}

# Function to run the frontend React app
run_frontend() {
    echo "Starting React app..."
    cd Frontend
    cd app
    ./run.sh &
    cd ..
}

# Run backend first, then frontend
run_backend
run_frontend

# Wait for all background processes to finish
wait
