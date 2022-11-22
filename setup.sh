#!/bin/sh

pip install rich

chmod +x ./offsync.sh

sudo mkdir -p /opt/offsync/

sudo cp -r ./offsync ./main.py ./LICENSE ./README.md /opt/offsync/

sudo cp ./offsync.sh /usr/local/bin/offsync

sudo chown -R "$(whoami):$(whoami)" /opt/offsync/

printf "\nNOW YOU CAN DELETE THIS REPO\n\n"

exit 0