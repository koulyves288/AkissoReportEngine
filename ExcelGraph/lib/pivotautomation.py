import pandas as pd

def generate_department_pivot_table(input_file, department):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Filter the DataFrame for the specified department
    df_department = df[df['Department'] == department]
    
    # Create a pivot table with Date as index and sum of 'Retard' and 'Depart anticipe' as values
    pivot_table = pd.pivot_table(df_department, index='Date', values=['Retard', 'Depart anticipe'], aggfunc='sum')
    
    # Add a row with the total of "Sum of Retard" and "Sum of Depart anticipe"
    pivot_table.loc['Total'] = pivot_table.sum()

    # Rename columns
    pivot_table = pivot_table.rename(columns={'Retard': 'Sum of Retard', 'Depart anticipe': 'Sum of Depart anticipe'})
    
    return pivot_table
def generate_department_employee_pivot_table(input_file, department):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Filter the DataFrame for the specified department
    df_department = df[df['Department'] == department]
    
    # Create a pivot table with Name as index and sum of 'Retard' and 'Depart anticipe' as values
    pivot_table = pd.pivot_table(df_department, index='Name', values=['Retard', 'Depart anticipe'], aggfunc='sum')
    
    # Add a row with the total of "Sum of Retard" and "Sum of Depart anticipe"
    pivot_table.loc['Total'] = pivot_table.sum()
    # Rename columns
    pivot_table = pivot_table.rename(columns={'Retard': 'Sum of Retard', 'Depart anticipe': 'Sum of Depart anticipe'})
    
    return pivot_table



