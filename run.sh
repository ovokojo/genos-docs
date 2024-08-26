#!/bin/bash

# Set the virtual environment name
VENV_NAME="venv"

# Check if virtual environment exists
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_NAME
fi

# Activate virtual environment
source $VENV_NAME/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment. Exiting."
    exit 1
fi

# Install or upgrade pip
pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing project dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi

# Install development dependencies if the file exists
if [ -f "requirements-dev.txt" ]; then
    echo "Installing development dependencies..."
    pip install -r requirements-dev.txt
else
    echo "requirements-dev.txt not found. Skipping development dependency installation."
fi

# Run the Streamlit app
echo " ______   ______"
echo "/  ____| |  __  \\"
echo "| |  __  | |  \\  |"
echo "| | |_ | | |   | |"
echo "| |__| | | |__/  |"
echo "\\______| |______/"
echo "Booting Genos Docs app.."
echo
python3 -m streamlit run app/app.py