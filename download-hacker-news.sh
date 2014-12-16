#!/bin/sh

WGET=$(which wget)
URLFILE="./urls-articles.txt"
CACHEDIR="./cache"

if [ ! -f "$URLFILE" ]
then
    echo "File '$URLFILE' not found. Aborting."
    exit 1
fi

if [ ! -d "$CACHEDIR" ]
then
    mkdir "$CACHEDIR"
    
    if [ ! -d "$CACHEDIR" ]
    then
        echo "Could not create cache directory '$CACHEDIR'. Aborting."
        exit 1
    fi
fi

$WGET --input-file "$FILEURLS" --output-directory "$CACHEDIR"

exit 0