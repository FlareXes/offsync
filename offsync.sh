#!/bin/sh

# Check if /opt/offsync/ directory does not exist
if ! [ -d /opt/offsync/ ]; then
  echo -e "\033[1;31mError: Offsync not installed.\033[0m" >&2
  exit 1
fi

# Check if /opt/offsync/main.py file does not exist
if ! [ -f /opt/offsync/main.py ]; then
  echo -e "\033[1;31mError: Failed to start offsync, '/opt/offsync/main.py' not found.\033[0m" >&2
  exit 1
fi

/opt/offsync/venv/bin/python3 /opt/offsync/main.py "$@"
