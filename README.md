# example opencv threshold filter tiles

## defaults

### Threshhold
The threshhold is set at 180, which seems to give a decent amount of lightness identification, 200 seemed to only identify 2 50px x 50px light spots per image

### Grid size

Grid size is configurable in process.py, right now it is set at 50px, assuming an average photo size is 750px x 750px

## pre-processing

The script assumes all images are png. There is a script in the pre-process folder that converts any image to png and crops to square and moves to the input folder for you.


