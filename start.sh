#!/usr/bin/env bash
set -euo pipefail

sudo docker-compose down --volumes --remove-orphans
sudo docker-compose build --no-cache
sudo docker-compose up -d

printf -- "- **Frontend:** http://localhost:2048\n"
printf -- "- **Backend API:** http://localhost:2049\n"
printf -- "- **Backoffice:** http://localhost:2050\n"
