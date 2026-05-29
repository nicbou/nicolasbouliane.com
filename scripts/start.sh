#!/usr/bin/env bash
source .env
set -e
set -x

cd site && ursus && ursus -wfs;