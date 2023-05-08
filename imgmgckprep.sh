identify $1
date=$(date -Iseconds)
convert $1 -quality 100% "temp.png"
convert temp.png -resize 100% -gravity Center "output-$date.png"
mv output*.png input_folder/
