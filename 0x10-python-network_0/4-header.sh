#!/bin/bash
# Sends a GET request to the URL, and displays the body of the respon
if [ "$(curl -sLw "%{http_code}" "$1" -o /dev/null)" -eq "200" ]; then curl -H "X-School-User-Id: 98" -sL "$1"; fi
