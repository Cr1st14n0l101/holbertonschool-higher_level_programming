#!/bin/bash
# Gets the HTTP code and If is 200 then display the body
if [ "$(curl -sLw "%{http_code}" "$1" -o /dev/null)" -eq "200" ]; then curl -sL "$1"; fi
