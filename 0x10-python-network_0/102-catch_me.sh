#!/bin/bash
# digs till it finds the message "You got me!" (Capture the flag?)
curl -X PUT -L "0.0.0.0:5000/catch_me_2" -H "Authorization: user_id" -d "user_id=98"
