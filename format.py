import csv
import re

# Input and output file paths
input_file = 'songs.csv'
output_file = 'output.csv'

# Read the input CSV file and write the formatted data to the output CSV file
with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
    # Create a CSV reader and writer with custom delimiters
    csv_reader = csv.reader(csv_input, delimiter=',')
    csv_writer = csv.writer(csv_output, delimiter=':')

    for row in csv_reader:
        # Define a regular expression pattern to find and remove text between brackets
        bracket_pattern = r'\[.*?\]'

        # Apply the pattern to each field in the row
        formatted_row = [re.sub(bracket_pattern, '', field) for field in row]

        # Replace newlines with semicolons in each field and write the row with the new delimiter
        formatted_row = [field.replace('\n', '; ').replace(
            '\u200b', '') for field in formatted_row]
        for i in range(3):
            formatted_row = [field.replace('; ; ', '; ').replace(
                '  ', ' ') for field in formatted_row]
        csv_writer.writerow(formatted_row)

print(f"CSV file formatted and saved as {output_file}")
