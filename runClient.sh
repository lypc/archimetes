#!/bin/bash

# This script is meant to start your metadata server

# Check the parameters provided
if [ "$#" -ne 4 ]
then
	echo "Wrong arguments, usage :"
	echo "./runClient.sh <config_file> <base_dir> <command> <filename>"
	exit
fi

CONFIGFILE_PATH=$1
DOWNLOAD_DIR=$2
COMMAND=$3
FILENAME_OR_UPLOADDIR=$4

# Now call your client with the above arguments
# Eg. If you are using python and your client is Client.py
# Call
#
python3 src/client.py $CONFIGFILE_PATH $DOWNLOAD_DIR $COMMAND $FILENAME_OR_UPLOADDIR
#
# or if CPP
#
# ./client $CONFIGFILE_PATH $DOWNLOAD_DIR $COMMAND $FILENAME_OR_UPLOADDIR