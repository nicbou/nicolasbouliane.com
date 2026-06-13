#!/bin/sh
set -e
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

log "Setting up webhooks for nicolasbouliane.com"

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "${PROJECT_ROOT}/.env"

log "Checking if webhook is installed"
if ! command -v webhook >/dev/null 2>&1; then
  log "Not installed. Installing webhook"
  apt update
  apt install -y webhook
fi

log "Creating webhook config"

mkdir -p /etc/webhook
mkdir -p /etc/systemd/system

HOOKS_FILE="/etc/webhook/hooks.yml"
cat <<EOF > "$HOOKS_FILE"
- id: deploy
  execute-command: ${PROJECT_ROOT}/.prod/deploy.sh
  command-working-directory: ${PROJECT_ROOT}
  trigger-rule:
    and:
      - match:
          type: payload-hash-sha256
          secret: ${GITHUB_WEBHOOK_SECRET}
          parameter:
            source: header
            name: X-Hub-Signature-256
      - match:
          type: value
          value: refs/heads/main
          parameter:
            source: payload
            name: ref
EOF

log "Creating webhook systemd service config"

SERVICE_FILE="/etc/systemd/system/webhook.service"
cat <<EOF > "$SERVICE_FILE"
[Unit]
Description=Webhooks for CI
After=network.target

[Service]
Type=simple
ExecStart=webhook -port 9000 -hooks "$HOOKS_FILE" -template -verbose
Restart=on-failure
PrivateTmp=true
User=root
[Install]
WantedBy=default.target
EOF

log "Installing and restarting webhook systemd service"

systemctl enable webhook
systemctl restart webhook

log "Setup done"
