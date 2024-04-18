import csv
import difflib


def extract_info_from_csv(file_path, contacts_number, contact_name):

    # Open the CSV file
    with open(file_path, "r") as file:
        reader = csv.DictReader(file, delimiter=",")
        counter = 0
        lines = 0
        for row in reader:
            lines += 1
            mobile = row["Mobile"]
            if mobile:
                closes_match = difflib.get_close_matches(
                    mobile, contact_numbers, cutoff=0.8
                )
                if len(closes_match) > 0:
                    index = contact_numbers.index(closes_match[0])
                    print(
                        f"Matches: {closes_match} \n Móvil Zoho: {mobile} \nContacto Zoho: {row['Last Name']} \nContacto Odoo: {contact_name[index]}"
                    )
                    print("---------------------------------------")
                else:
                    counter += 1
        return counter, lines


# Example usage
file_path_Odoo = "norm_files/exported_Odoo/Contacto-Odoo.csv"  # Change this to the path of your CSV file
file_path_Zoho = "norm_files/exported_Zoho/Contacto-Zoho.csv"  # Change
contact_numbers = []
contact_name = []
with open(file_path_Odoo, "r", encoding="latin-1") as file:
    reader = csv.DictReader(file, delimiter=";")
    counter = 0
    for row in reader:
        contact_numbers.append(row["Telefono"])
        contact_name.append(row["Nombre mostrado"])

count, lines = extract_info_from_csv(file_path_Zoho, contact_numbers, contact_name)
print(
    f"Cant. contactos Odoo: {len(contact_numbers)} \nContactos no encontrados: {count} \nCant. Contactos Zoho: {lines} \nContactos encontrados: {lines - count}"
)
