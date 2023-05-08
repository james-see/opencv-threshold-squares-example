#!/bin/bash
# This script reads in a filename or filename and path and converts to png and crops it square and moves it to input_folder naming it with time and date
identify $1
date=$(date -Iseconds)
convert $1 -quality 100% "temp.png"
convert temp.png -resize 100% -gravity Center "square-$date.png"
mv output*.png ../input_folder/
