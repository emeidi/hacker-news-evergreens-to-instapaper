#!/bin/sh

WGET=$(which wget)
URLFILE="./urls-hacker-news.txt"
CACHEDIR="./cache"

if [ ! -f "$URLFILE" ]
then
    echo "File '$URLFILE' not found. Aborting."
    exit 1
fi

if [ ! -d "$CACHEDIR" ]
then
    mkdir -p "$CACHEDIR"
    
    if [ ! -d "$CACHEDIR" ]
    then
        echo "Could not create cache directory '$CACHEDIR'. Aborting."
        exit 1
    fi
fi

echo "Downloading URLs found in file '$URLFILE' to cache directory '$CACHEDIR' ..."

$WGET --input-file "$URLFILE" --directory-prefix "$CACHEDIR"

echo "Done."
echo ""

exit 0