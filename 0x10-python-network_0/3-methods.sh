#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -i -sX OPTIONS -L "$1" | grep 'Allow' | cut -c8-
