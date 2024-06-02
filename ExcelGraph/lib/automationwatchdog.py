import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from lib.automation import *
#from chartsengine import generate_excel_chart
from lib.chartsengine import generate_department_depart_excel_chart, generate_department_retard_excel_chart
from lib.pivotautomation import generate_department_employee_pivot_table

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, folder_path, callback):
        super().__init__()
        self.folder_path = folder_path
        self.callback = callback
    
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.csv'):
            self.callback(event.src_path)

def watch_folder(folder_path, callback):
    event_handler = FileEventHandler(folder_path, callback)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def csv_file_callback(file_path):
    print(f"CSV file '{file_path}' picked up.")
   
    input_file = file_path
    output_file = 'absent_out_file.csv'
    output2_file = 'retard_out_file.csv'
    output3_file = 'cleansed_out_file.csv'
    add_absent_column(input_file, output_file)
    add_retard_column(output_file, output2_file)
    add_depart_anticipe_column(output2_file, output3_file)

    #Replace 'input_file.csv' with the path to your input CSV file
    input_file = 'cleansed_out_file.csv'
    department_column='Department'
    # generate_report_by_department(input_file,department_column)
    # generate_report_by_department_employee(input_file,department_column)
    # generate_report_by_department_retard(input_file,department_column)
    # generate_report_by_department_depart(input_file,department_column)
    generate_report_by_department_absent(input_file,department_column)
    generate_report_by_department_absent_forperiod(input_file,department_column)
    generate_report_by_department_byemployee_retard(input_file,department_column)
    generate_report_by_department_forperiod_retard(input_file,department_column)
    generate_report_by_department_forperiod_depart(input_file,department_column)
    generate_report_by_department_byemployee_depart(input_file,department_column)
    generate_final_report(input_file,department_column)

