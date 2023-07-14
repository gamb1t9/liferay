#!/bin/sh
echo "$(date)" > creation_date
mkdir templates static static/uploads
mv index.html templates/
exec python app.py
