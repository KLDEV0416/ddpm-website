#!/usr/bin/env bash
# Publish the latest DDPM website from GitHub. Run as the deploy user on the VPS:
#   /srv/ddpm/site/deploy/update.sh
set -euo pipefail
cd /srv/ddpm/site
git fetch --prune origin
git reset --hard origin/main
echo "ddpm.com.my now on $(git log -1 --pretty='%h %s')"
