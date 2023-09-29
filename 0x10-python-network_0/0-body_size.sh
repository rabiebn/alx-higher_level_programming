#!/bin/bash
# Display size of message body of response.
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
