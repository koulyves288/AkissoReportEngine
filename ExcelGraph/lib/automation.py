import csv
import json


from lib.chartsengine import generate_department_byemployee_absent_excel_chart, generate_department_byemployee_depart_excel_chart, generate_department_byemployee_retard_excel_chart, generate_department_depart_excel_chart, generate_department_employee_excel_chart, generate_department_excel_chart, generate_department_forperiod_absent_excel_chart, generate_department_forperiod_depart_excel_chart, generate_department_forperiod_retard_excel_chart, generate_department_retard_excel_chart
from lib.pivotautomation import generate_department_byemployee_depart_pivot_table, generate_department_byemployee_retard_pivot_table, generate_department_employee_absence_pivot_table, generate_department_employee_pivot_table, generate_department_forperiod_absence_pivot_table, generate_department_forperiod_depart_pivot_table, generate_department_forperiod_retard_pivot_table, generate_department_pivot_table
from pathlib2 import Path 
import pdfkit 
import pandas as pd

def parse_absenteeism(row):
    remark = row["Remark"]
    if "Absence" in remark:
        # Extracting hours or minutes from the "Remark" column
        if "Hours" in remark:
            return float(remark.split(":")[1].split("Hours")[0])
        elif "Minutes" in remark:
            return float(remark.split(":")[1].split("Minutes")[0]) / 60
    return None

def parse_lateineism(row):
    remark = row["Remark"]
    if "Late In" in remark:
        
        # Extracting hours or minutes from the "Remark" column
        if "Hours" in remark:
            return float(remark.split(":")[1].split("Hours")[0])
        elif "Minutes" in remark:
           
            return float(remark.split(":")[1].split("Minutes")[0])
    return None
def parse_earlyouteism(row):
    remark = row["Remark"]
    if "Early Out" in remark:
        
        # Extracting hours or minutes from the "Remark" column
        if "Hours" in remark:
            return float(remark.split(":")[1].split("Hours")[0])
        elif "Minutes" in remark:
           
            return float(remark.split(":")[1].split("Minutes")[0])
    return None
def add_absent_column(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['Absent'])
        writer.writeheader()
        for row in reader:
            absent_hours = parse_absenteeism(row)
            row['Absent'] = absent_hours if absent_hours is not None else ''
            writer.writerow(row)
def add_retard_column(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Retard']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            absent_hours = parse_absenteeism(row)
            latein_minutes= parse_lateineism(row)
            if absent_hours is None:
                row['Retard'] = 0
                if latein_minutes is None:
                    row['Retard']=0
                elif "Late In" in row['Remark'] and latein_minutes > 1:
                    row['Retard']=1
            else:
                if 0 < absent_hours <= 1:
                    row['Retard'] = 1
                else:
                    row['Retard'] = 0
            writer.writerow(row)

def add_depart_anticipe_column(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Depart anticipe']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            absent_hours = parse_absenteeism(row)
            earlyout_minutes= parse_earlyouteism(row)
            if absent_hours is None:
                row['Depart anticipe'] = 0
                if earlyout_minutes is None:
                    row['Depart anticipe']=0
                elif "Early Out" in row['Remark'] and earlyout_minutes > 1:
                    row['Depart anticipe']=1
            else:
                row['Depart anticipe'] = 0
                
            writer.writerow(row)
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
def get_unique_column_values(csv_file, column_name):
    unique_values = set()  # Using a set to store unique values
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            unique_values.add(row[column_name])
    
    return list(unique_values)
def generate_report_by_department(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_excel_chart(pivot_table,department)

def generate_report_by_department_employee(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_employee_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department Employee:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_employee_excel_chart(pivot_table,department)

def generate_report_by_department_retard(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department Employee:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_retard_excel_chart(pivot_table,department)
def generate_report_by_department_depart(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department Employee:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_depart_excel_chart(pivot_table,department)
def generate_report_by_department_absent(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_employee_absence_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department Employee Absent:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_byemployee_absent_excel_chart(pivot_table,department)

def generate_report_by_department_absent_forperiod(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_forperiod_absence_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department For Period Absent:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_forperiod_absent_excel_chart(pivot_table,department)

def generate_report_by_department_byemployee_retard(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_byemployee_retard_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department For Retard By Empoyee:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_byemployee_retard_excel_chart(pivot_table,department)

def generate_report_by_department_forperiod_retard(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_forperiod_retard_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department For Retard By Empoyee:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_forperiod_retard_excel_chart(pivot_table,department)

def generate_report_by_department_forperiod_depart(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_forperiod_depart_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department For Depart By Period:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_forperiod_depart_excel_chart(pivot_table,department)

def generate_report_by_department_byemployee_depart(input_file,department_column):
    
    unique_column_values = get_unique_column_values(input_file, department_column)
    for department in unique_column_values:
        # Generate the pivot table
        pivot_table = generate_department_byemployee_depart_pivot_table(input_file, department)
        # Print the pivot table
        print("Pivot Table for Department For Depart By Period:", department)
        print(pivot_table)
        # Replace 'pivot_table' with the pivot table generated from the previous function
        generate_department_byemployee_depart_excel_chart(pivot_table,department)
def generate_final_report(input_file, department_column):
    unique_column_values = get_unique_column_values(input_file, department_column)
    html_report='reports/html/'
    final_report='reports/final/'
    departmentpc="{{reportdepartment}}"
    periodstart='{{periodstart}}'
    periodend='{{periodend}}'

    for department in unique_column_values:
      
        with open('report_template.html', 'r', encoding='utf-8') as file:
            html_stringo = file.read()
            print(html_stringo)
            charts={
                    'chart1':'../department_absent/'+department+'.png',
                    'chart2':'../department_absent_period/'+department+'.png',
                    'chart3':'../department_retard_byemployee/'+department+'.png',
                    'chart4':'../department_retard_forperiod/'+department+'.png',
                    'chart5':'../department_depart_byemployee/'+department+'.png',
                    'chart6':'../department_depart_forperiod/'+department+'.png'
                }   
            search=['chart1','chart2','chart3','chart4','chart5','chart6']
            modified_html_content=html_stringo
            
            for searchword in search:
                print(searchword)
                modified_html_content = modified_html_content.replace(searchword, charts[searchword])
            mindate=get_min_date(input_file,'Date')
            maxdate=get_max_date(input_file,'Date')
            modified_html_content=modified_html_content.replace(departmentpc,department).replace(periodstart,mindate).replace(periodend,maxdate)
            print(modified_html_content)        
            html_file=html_report+department+'.html'
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(modified_html_content)
            #print(final_report+department+'.pdf')
            pdfkit.from_file(input=html_file, output_path=final_report+department+'.pdf',options={"enable-local-file-access": ""})      
                            


def get_min_date(file_path, column_name):
   
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Convert the specified column to datetime
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
        
        # Drop rows where the conversion failed (NaT values)
        df = df.dropna(subset=[column_name])
        
        # Find the minimum date
        min_date = df[column_name].min()
        
        # Return the minimum date in YYYY-MM-DD format
        return min_date.strftime('%d-%m-%Y')
    except KeyError:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
def get_max_date(file_path, column_name):
   
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Convert the specified column to datetime
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
        
        # Drop rows where the conversion failed (NaT values)
        df = df.dropna(subset=[column_name])
        
        # Find the minimum date
        max_date = df[column_name].max()
        
        # Return the minimum date in YYYY-MM-DD format
        return max_date.strftime('%d-%m-%Y')
    except KeyError:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
