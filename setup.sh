#!/usr/bin/env bash

# Print text in colored format
log_echo() {
  # $1 is the text to print
  # $2 is the color of the text

  if [ "$2" == "red" ]; then
    # Print the text in red
    echo -e "\033[1;31m$1\033[0m" >&2
    exit 1

  elif [ "$2" == "green" ]; then
    # Print the text in green
    echo -e "\033[1;32m$1\033[0m"

  else
    # If the color is not recognized, print the text in the default color
    echo "$1"
  fi
}

# Make the offsync.sh script executable
if ! chmod +x ./offsync.sh; then
  log_echo "Error: Failed to make the offsync.sh executable" "red"
fi

# Create the /opt/offsync/ directory if it does not exist
if ! [ -d /opt/offsync/ ]; then
  if ! sudo mkdir -p /opt/offsync/; then
    log_echo "Error: Failed to create the /opt/offsync/ directory" "red"
  fi
fi

# Make the /opt/offsync/ directory owned by the current user
if ! sudo chown -R "$(whoami):$(whoami)" /opt/offsync/; then
  log_echo "Error: Failed to change ownership of /opt/offsync/" "red"
fi

# Create the /usr/share/licenses/offsync/ directory if it does not exist
if ! [ -d /usr/share/licenses/offsync/ ]; then
  if ! sudo mkdir -p /usr/share/licenses/offsync/; then
    log_echo "Error: Failed to create the /usr/share/licenses/offsync/ directory" "red"
  fi
fi

# Copy the necessary files and directories to /opt/offsync/
if ! cp -r ./offsync ./main.py ./LICENSE ./README.md ./requirements.txt /opt/offsync/; then
  log_echo "Error: Failed to copy files to /opt/offsync/" "red"
fi

# Copy the LICENSE to /usr/share/licenses/offsync/
if ! sudo cp ./LICENSE /usr/share/licenses/offsync/; then
  log_echo "Error: Failed to copy LICENSE to /usr/share/licenses/offsync/" "red"
fi

# Copy the offsync.sh script to /usr/local/bin/offsync
if ! sudo cp ./offsync.sh /usr/local/bin/offsync; then
  log_echo "Error: Failed to copy the offsync.sh script to /usr/local/bin/offsync" "red"
fi

# Create python virtual environment to install dependencies
if ! python3 -m venv /opt/offsync/venv; then
  log_echo "Error: Failed to create virtual environment of /opt/offsync/" "red"
fi

# Install dependencies
if ! /opt/offsync/venv/bin/python3 -m pip install -r /opt/offsync/requirements.txt; then
  log_echo "Error: Failed to install the dependencies" "red"
fi

log_echo "Now you can delete cloned repository" "green"
