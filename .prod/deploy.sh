#!/bin/sh
set -e
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

mkdir -p /var/log/nicolasbouliane
exec >> "/var/log/nicolasbouliane/deploy.log" 2>&1

log "Deploying nicolasbouliane.com"

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$PROJECT_ROOT"

log "Pulling new changes"
git reset --hard && git pull origin main

log "Rebuilding project"
docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

log "Pruning old docker images"
docker image prune -a -f
docker builder prune -f

log "Reinstalling production deployment scripts"
${PROJECT_ROOT}/.prod/setup.sh
