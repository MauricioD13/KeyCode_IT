import csv
import difflib


def extract_info_from_csv(file_path_Zoho, file_path_Odoo):
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

    # Open the CSV file
    with open(file_path_Zoho, "r") as file_zoho, open(
        file_path_Odoo, "r"
    ) as file_Odoo, open("contact_to_import_create.csv", "w") as output_file:
        reader_zoho = csv.DictReader(file_zoho, delimiter=",")
        reader_odoo = csv.DictReader(file_Odoo, delimiter=";")
        writer = csv.writer(output_file)
        counter = 0
        lines = 0
        mobiles_zoho = []
        writer.writerow(
            ["Nombre de contacto", "mobile", "mail", "pais", "Verificado Odoo"]
        )
        for row in reader_zoho:
            mobiles_zoho.append(row["Mobile"])

        for row_odoo in reader_odoo:
            lines += 1
            mobile = row_odoo["Telefono"]
            if mobile:
                closes_match = difflib.get_close_matches(
                    mobile, mobiles_zoho, cutoff=0.8
                )
                if len(closes_match) <= 0:
                    text = row_odoo["Nombre mostrado"].lower()
                    row_empty = False
                    row_name = False
                    if not any(keyword in text for keyword in keywords):
                        row_name = True
                    if row_odoo["Telefono"] == "":
                        row_empty = True
                    if row_name == True and row_empty == False:
                        writer.writerow(
                            [
                                row_odoo["Nombre mostrado"],
                                f"{mobile}",
                                row_odoo["Correo electronico"],
                                row_odoo["Pais"],
                                "true",
                            ]
                        )

                    counter += 1
        return counter, lines


# Example usage
file_path_Odoo = "norm_files/exported_Odoo/Contacto-Odoo.csv"  # Change this to the path of your CSV file
file_path_Zoho = "norm_files/exported_Zoho/Contacto-Zoho.csv"  # Change

count, lines = extract_info_from_csv(file_path_Zoho, file_path_Odoo)
print(
    f"Contactos no encontrados: {count} \nCant. Contactos Zoho: {lines} \nContactos encontrados: {lines - count}"
)
