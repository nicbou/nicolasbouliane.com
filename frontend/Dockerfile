FROM ghcr.io/astral-sh/uv:0.9.1-python3.13-bookworm-slim AS base

RUN apt-get update \
    && apt-get install -y --no-install-recommends git rsync \
        build-essential \
        python3-dev \
    && mkdir -p /var/output \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN uv pip install --system --no-cache -r /requirements.txt \
    && rm /requirements.txt

ENV URSUS_OUTPUT_DIR=/var/output

WORKDIR /var/project/frontend

# = PROD =======================================================================

FROM base AS prod
CMD python3 /var/project/frontend/build-for-prod.py

# = DEV ========================================================================

FROM base AS dev

CMD rm -f /tmp/build_finished;\
    ursus;\
    touch /tmp/build_finished;\
    ursus --fast --watch

# Container becomes healthy after initial build
HEALTHCHECK --start-interval=1s --start-period=15m \
  CMD [ -f /tmp/build_finished ] || exit 1
