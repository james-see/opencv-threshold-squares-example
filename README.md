# example opencv threshold filter tiles

This repo takes in a folder of png images and splits them up into grids per image and identifies light areas in the grid and creates output images with the grid overlaid as well as a csv of the stats.
## quickstart

1. install opencv-python via `pip3 install opencv-python`
2. run process.py or process-nongreen.py for use case
3. check the output.csv and the output_folder
4. Adjust threshholds as needed for use case
## defaults

### Threshholds

#### process script for lightness filter
The threshhold is set at 180, which seems to give a decent amount of lightness identification, 200 seemed to only identify 2 50px x 50px light spots per image

#### process script for green filter

The threshhold is set as 0.2 * average greenness of each photo to account for the relative denseness of each and adjust, since some photos are naturally greener.

### Grid size

Grid size is configurable, right now it is set at 50px, assuming an average photo size is 750px x 750px
25px seems to also be a good default.

## pre-processing

The script assumes all images are png. There is a script in the pre-process folder that converts any image to png and crops to square and moves to the input folder for you.

## output

The images are output to output_folder and a csv of the image name, the white square count, and the total squares is output to output.csv
### ChatGPT

prompts in order (each one I executed, copied the code and then tweaked it some more):

i need opencv python code to split up a png image into 50px grid and identify the light and dark squares and fill in the squares in white that are lighter than most. the image is 750x750px

I need it to also print the total number of white squares in the bottom right on the image

i need to save the image out instead of opening it and store the image name, total white squares, and total squares in a csv called output.csv instead of showing it

i need to iterate through an input folder of png images and do the same thing for each with the images numbered output1.png output2.png etc.

i need it to not do the threshhold based on the image average but by a static lightness value

instead of the lightness threshhold, I need a not-greeness threshhold, areas that are not shades of green

I needs to figure out the average green per photo instead of using a static threshhold

_and that is all!_

### Example output at 50px squares

<img width="520" alt="Screenshot 2023-05-08 at 7 58 03 PM" src="https://user-images.githubusercontent.com/616585/236961581-aa4e2ab2-cb3e-4a0a-9413-a0872696ae75.png">
<img width="554" alt="Screenshot 2023-05-08 at 7 57 54 PM" src="https://user-images.githubusercontent.com/616585/236961589-5323ec23-6587-46f0-aa92-768138be6ba8.png">



