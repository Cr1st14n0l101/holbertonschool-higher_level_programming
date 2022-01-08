#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the response
curl -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -sLX POST "$1"
