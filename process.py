import cv2
import numpy as np
import os
import csv

# Define the input folder and output folder paths
input_folder = 'input_folder'
output_folder = 'output_folder'

# Define the grid size and lightness threshold
grid_size = 50
lightness_threshold = 180

# Loop over each file in the input folder
for i, filename in enumerate(os.listdir(input_folder)):
    # Check if the file is a PNG image
    if filename.endswith('.png'):
        # Load the image
        img = cv2.imread(os.path.join(input_folder, filename))

        # Calculate the number of rows and columns in the grid
        rows, cols, _ = img.shape
        num_rows = rows // grid_size
        num_cols = cols // grid_size

        # Loop over each grid square
        num_white_squares = 0
        for i in range(num_rows):
            for j in range(num_cols):
                # Calculate the start and end indices of the grid square
                start_row = i * grid_size
                end_row = start_row + grid_size
                start_col = j * grid_size
                end_col = start_col + grid_size

                # Extract the grid square
                square = img[start_row:end_row, start_col:end_col]

                # Calculate the average lightness value for the grid square
                lightness = np.mean(cv2.cvtColor(square, cv2.COLOR_BGR2GRAY))

                # If the lightness value is above the threshold, fill in the grid square with white
                if lightness > lightness_threshold:
                    img[start_row:end_row, start_col:end_col] = [255, 255, 255]
                    num_white_squares += 1

        # Save the output image with a numbered file name
        output_name = f'output{i+1}.png'
        cv2.imwrite(os.path.join(output_folder, output_name), img)

        # Calculate the total number of squares
        total_squares = num_rows * num_cols

        # Store the image name, total white squares, and total squares in a CSV file
        with open('output.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([output_name, num_white_squares, total_squares])
