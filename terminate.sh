#!/bin/bash

# Function to terminate processes running on specified ports
terminate() {
    local PORT=$1
    local PID=$(lsof -ti:$PORT)

    if [ ! -z "$PID" ]; then
        echo "Terminating process $PID on port $PORT"
        kill -9 $PID
    fi
}
