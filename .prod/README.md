# Deployment to production

Deployments are triggered by a GitHub webhook. It requires `webhook` to be installed and running. The webhook runs at `http://nicolasbouliane.com:9000/hooks/deploy`.

`webhook` runs as a systemd socket and service. To see the `webhook` logs, run `journalctl -u webhook.service` and `journalctl -u webhook.socket`.

## Setup

1. Clone this repository
2. Create a `.env` file in your project root. Use `.env.example` as a template.
3. Run `setup.sh`.