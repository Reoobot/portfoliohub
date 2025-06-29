#!/bin/sh
TIMESTAMP=$(date +"%Y%m%d%H%M")
tar -czf /backup/portfoliohub-$TIMESTAMP.tar.gz /usr/share/nginx/html
