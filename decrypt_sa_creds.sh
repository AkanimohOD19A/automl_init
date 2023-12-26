#!/bin/bash
# Decrypt the file
mkdir $HOME/secrets
gpg --quiet --batch --yes --decrypt --passphrase="$SA_CREDS_PASSPHRASE" \
--output $HOME/secrets/sa-creds.json sa-creds.json.gpg

