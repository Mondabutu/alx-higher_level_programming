#!/bin/bash
# This end a request to an URL with curl, and displays the size of the body of the response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
