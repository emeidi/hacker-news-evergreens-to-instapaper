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
    mkdir -p "$CACHEDIR"
    
    if [ ! -d "$CACHEDIR" ]
    then
        echo "Could not create cache directory '$CACHEDIR'. Aborting."
        exit 1
    fi
fi

echo "Downloading URLs found in file '$FILEURLS' to cache directory '$CACHEDIR' ..."

$WGET --input-file "$FILEURLS" --output-directory "$CACHEDIR"

echo "Done."
echo ""

exit 0