#!/bin/bash
echo "COUNTER=\$COUNTER+1" >> counter.sh

curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=/home/ec2-user/django/initial_meme_stock/${COUNTER}.png" http://3.83.27.88:8000/upload
