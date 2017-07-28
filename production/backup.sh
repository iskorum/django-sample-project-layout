#!/bin/bash

export LC_ALL="en_US.UTF-8"

BACKUP_DIR="/home/{{ project_name }}/backup/db"
TIMESTAMP=`date +%F-%H%M`
BACKUP_NAME="$TIMESTAMP.sql"

mkdir -p $BACKUP_DIR


pg_dump -Fc {{ project_name }} > $BACKUP_NAME

tar -zcvf $BACKUP_DIR/$TIMESTAMP.tgz $BACKUP_NAME

rm $BACKUP_NAME
