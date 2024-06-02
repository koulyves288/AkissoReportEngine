
from lib.automationwatchdog import *
import pdfkit 

# Replace 'input_file.csv' with the path to your input CSV file
# Replace 'output_file.csv' with the desired path for the output CSV file

#load config file:
file_path = 'lib/config.json'

# Read JSON properties
json_data = read_json_file(file_path)
for key, value in json_data.items():
    print(f"{key}: {value}")

folder_to_watch = json_data['watchdogfolder']
watch_folder(folder_to_watch, csv_file_callback)
#pdfkit.from_file(input='report_template.html', output_path='example.pdf',options={"enable-local-file-access": ""}) 
# print(f"Watching folder: {folder_to_watch}")
# droppedfile=watch_folder(folder_to_watch, csv_file_callback)
# print(droppedfile)


