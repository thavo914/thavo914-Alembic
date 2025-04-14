import pandas as pd
import os
import sys

# Fix the path resolution by going up two levels from TK5491 directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
excel_path_QT = os.path.join(project_root, "data", "inactive_doi-ten-dich-vu_hdyk_14-04-2025_1744602249.xlsx")

# Load the Excel file
xls = pd.ExcelFile(excel_path_QT)

# Print available sheet names
print(xls.sheet_names)

# Read the first sheet explicitly using the sheet name
first_sheet_df = pd.read_excel(xls, sheet_name='Đổitên')

# Display the first few rows
# print(first_sheet_df.head())
print(first_sheet_df)
