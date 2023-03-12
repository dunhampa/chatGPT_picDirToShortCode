import os
import sys

# Get the directory and output file name from the command line arguments
directory = sys.argv[1]
output_file_name = sys.argv[2]

# Open a file for writing the output
output_file = open(output_file_name, 'w')

# Iterate through the files in the directory
for filename in os.listdir(directory):
  # Format the string with the file name and write it to the output file
  output_string = '{{{{<imageToClickGlobal imgPosition = "left"  Caption = "{}" imagePath = "/img/{}"  width = "60%" >}}}}\n'.format(filename, filename)
  output_file.write(output_string)

# Close the output file
output_file.close()

