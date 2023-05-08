# example opencv threshold filter tiles

This repo takes in a folder of png images and splits them up into grids per image and identifies light areas in the grid and creates output images with the grid overlaid as well as a csv of the stats.
## quickstart

1. install opencv-python via `pip3 install opencv-python`
2. run process.py
3. check the output.csv and the output_folder
4. Adjust threshholds as needed for use case
## defaults

### Threshhold
The threshhold is set at 180, which seems to give a decent amount of lightness identification, 200 seemed to only identify 2 50px x 50px light spots per image

### Grid size

Grid size is configurable in process.py, right now it is set at 50px, assuming an average photo size is 750px x 750px

## pre-processing

The script assumes all images are png. There is a script in the pre-process folder that converts any image to png and crops to square and moves to the input folder for you.

## output

The images are output to output_folder and a csv of the image name, the white square count, and the total squares is output to output.csv
### ChatGPT

prompts in order:

i need opencv python code to split up a png image into 50px grid and identify the light and dark squares and fill in the squares in white that are lighter than most. the image is 750x750px

I need it to also print the total number of white squares in the bottom right on the image

i need to save the image out instead of opening it and store the image name, total white squares, and total squares in a csv called output.csv instead of showing it

i need to iterate through an input folder of png images and do the same thing for each with the images numbered output1.png output2.png etc.

i need it to not do the threshhold based on the image average but by a static lightness value

_and that is all!_

