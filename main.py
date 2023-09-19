from pathlib import Path

import pandas as pd  


output_dir = Path(__file__).parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)


excel_file = Path(__file__).parent / "new_emp.xlsx"

df = pd.read_excel(excel_file)
column_name = "Emp_no"
col_name="Name"
unique_values = df[column_name].unique()
# print(type(unique_values))
# print(unique_values)
# for item in unique_values:
#     print(item)
for unique_value in unique_values:
    df_output = df[df[column_name] == unique_value]
    df_output['firstnames'] = df_output.Name.str.split('\s+').str[0]
    df_output['lastnames'] = df_output.Name.str.split('\s+').str[-1]
    new_Sal=df_output.Salary
    new_Sal+=new_Sal/10
    df_output['New_salary']=new_Sal
    # df_output['lastnames']=df_output['Name'].str.split(n = 0, expand = False).str[1]
    df_output=df_output.drop(['Name'], axis=1)
    output_path = output_dir / f"{unique_value}.xlsx"
    df_output.to_excel(output_path, sheet_name=str(unique_value), index=False)