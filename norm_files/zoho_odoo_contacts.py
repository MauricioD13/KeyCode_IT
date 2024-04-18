import csv


def extract_info_from_csv(file_path_Odoo, file_accounts_Zoho, file_contacts_Zoho):
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
        file_accounts_Zoho, "w"
    ) as outfile_accounts, open(file_contacts_Zoho, "w") as outfile_contacts:
        reader = csv.DictReader(file, delimiter=";")
        writer = csv.DictWriter(
            outfile_accounts, fieldnames=reader.fieldnames, delimiter=","
        )
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
                if int(row["Rango de proveedor"]) > 0:
                    outfile_accounts.write(
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
file_path_Odoo = (
    "norm_files/exported_Odoo/Contacto-Odoo.csv"  # Change this to the path of your CSV file
)
file_accounts_Zoho = "norm_files/CuentasImportacion.csv"
file_contacts_Zoho = "norm_files/ContactosImportacion.csv"
extract_info_from_csv(file_path_Odoo, file_accounts_Zoho, file_contacts_Zoho)
