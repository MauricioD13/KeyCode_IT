import csv


def extract_info_from_csv(file_path_Odoo, file_path_Zoho):
    # Open the CSV file

    keywords = [
        "NO USAR",
        "no usar",
        "Bloqueado",
        "facturar",
        "*bloqueado*",
        "* falta dni*",
        "*baja*",
        "*falta dni*",
        "*deuda*",
    ]

    with open(file_path_Odoo, "r", encoding="latin-1") as file, open(
        file_path_Zoho, "w"
    ) as outfile:
        reader = csv.DictReader(file, delimiter=";")
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter=",")
        writer.writeheader()
        counter = 0
        for row in reader:
            text = row["Nombre mostrado"].lower()
            row_empty = False
            row_name = False
            if not any(keyword in text for keyword in keywords):
                row_name = True
            if row["Teléfono"] == "" and row["Correo electrónico"] == "":
                row_empty = True

            if row_name == True and row_empty == False:
                outfile.write(
                    row["Nombre mostrado"]
                    + ","
                    + row["Teléfono"]
                    + ","
                    + row["Correo electrónico"]
                    + ","
                    + "Cuello"
                    + ","
                    + row["País"]
                    + "\n"
                )
                # "Account Id","Nombre de Cuenta",Phone,Email,Website,"Propietario de Cuenta","Propietario de Cuenta Id",Fax,Industry,"Annual Revenue","Created By","Created By Id","Modified By","Modified By Id","Created Time","Modified Time",Street,City,State,Code,Country,Description
                # print(f"{row['Nombre mostrado']}")


# Example usage
file_path_Odoo = "Contacto_companies.csv"  # Change this to the path of your CSV file
file_path_Zoho = "CuentasImportacion.csv"
extract_info_from_csv(file_path_Odoo, file_path_Zoho)
