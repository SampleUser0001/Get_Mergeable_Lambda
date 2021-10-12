#!/bin/bash

ARCHIVE_NAME=lambda_app
ARCHIVE_FILE=$ARCHIVE_NAME".zip"

if [ -e $ARCHIVE_FILE ]; then
  rm $ARCHIVE_FILE
fi


# 今の所、Boto3しか必要なものがないので、これだけでOK。
zip $ARCHIVE_NAME lambda_function.py
# zip $ARCHIVE_NAME lib lambda_function.py
