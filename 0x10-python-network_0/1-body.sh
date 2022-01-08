#!/bin/bash
# Gets the HTTP code and If is 200 then display the body
if [ "$(curl -sI "$1" | grep '200' | awk '{print $2}')" == '200' ]; then curl "$1"; fi
