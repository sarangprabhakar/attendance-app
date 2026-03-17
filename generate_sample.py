"""Run this to generate a sample attendance Excel file for testing."""
from openpyxl import Workbook
from datetime import date

wb = Workbook()
ws = wb.active
ws.title = "Week1"

headers = ['Reg No', 'Student Name', date(2024,1,15), date(2024,1,16), date(2024,1,17), date(2024,1,18), date(2024,1,19)]
ws.append(headers)

students = [
    ['CS001', 'Alice Johnson', 'P', 'P', 'A', 'P', 'P'],
    ['CS002', 'Bob Smith',     'A', 'P', 'P', 'A', 'P'],
    ['CS003', 'Carol White',   'P', 'A', 'P', 'P', 'P'],
    ['CS004', 'David Lee',     'P', 'P', 'P', 'A', 'P'],
    ['CS005', 'Eva Brown',     'P', 'A', 'P', 'P', 'A'],
]
for s in students:
    ws.append(s)

wb.save('sample_attendance.xlsx')
print("✅ sample_attendance.xlsx created!")
