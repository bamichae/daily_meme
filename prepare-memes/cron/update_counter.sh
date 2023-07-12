#!/bin/bash
echo "COUNTER=\$COUNTER+1" >> counter.sh

curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=/home/ec2-user/django/django-images/prepare-memes/daily-meme-preparer/output/${COUNTER}.png" http://3.83.27.88:8000/upload
