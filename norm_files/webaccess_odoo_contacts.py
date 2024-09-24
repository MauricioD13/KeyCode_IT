import pandas as pd

inputExcelFile = "Contactos_odoo.xlsx"

excelFile = pd.read_excel(inputExcelFile)

excelFile.to_csv("Contactos_odoo.csv",index=None, header=True)



