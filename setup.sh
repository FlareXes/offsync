#!/bin/sh

pip install -r requirements.txt

chmod +x ./offsync.sh

sudo mkdir -p /opt/offsync/

sudo cp -r ./offsync ./main.py ./LICENSE ./README.md /opt/offsync/

sudo cp ./offsync.sh /usr/local/bin/offsync

sudo chown -R "$(whoami):$(whoami)" /opt/offsync/

printf "\n\nNOW YOU CAN DELETE THIS REPO\n"

exit 0