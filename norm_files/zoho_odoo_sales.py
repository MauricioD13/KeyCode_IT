import csv
import re


def organize_SN(custom_note):
    filters = ["<p>", "<br>", "</p>"]
    custom_note = custom_note.replace(" ", "")
    regex = r"(?<=<p>)(.*?)(?=<br></p>)"
    serialNumber = re.findall(regex, custom_note, re.MULTILINE)
    return serialNumber


def extract_info_from_csv(file_path_Odoo, file_Zoho):
    # Open the CSV file
    with open(file_path_Odoo, "r", encoding="latin-1") as file, open(
        file_Zoho, "w"
    ) as outfile:
        reader = csv.DictReader(file, delimiter=";")
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter=",")
        writer.writeheader()
        counter = 0
        for row in reader:
            serialNumber = organize_SN(row["Custom Note"])
            if serialNumber != [""] and serialNumber:
                serialNumber = serialNumber[0]
                serialNumber = serialNumber.replace("</p>", "")
                serialNumber = serialNumber.replace("<p>", "")
                """if re.search(":", serialNumber):
                    serialNumber = serialNumber.split(":")
                    print(f"SN {serialNumber} Cliente: {row['Cliente']}")
                else:
                    print(f"SN [{serialNumber}] Cliente: {row['Cliente']}")"""
            if row["Estado"] == "Pedido de venta":
                if serialNumber == [""]:
                    serialNumber = "N/A"
                try:

                    outfile.write(
                        row["Referencia del pedido"]
                        + ","
                        + row["Cliente"]
                        + ","
                        + serialNumber
                        + "\n"
                    )
                except:
                    continue
            # "Account Id","Nombre de Cuenta",Phone,Email,Website,"Propietario de Cuenta","Propietario de Cuenta Id",Fax,Industry,"Annual Revenue","Created By","Created By Id","Modified By","Modified By Id","Created Time","Modified Time",Street,City,State,Code,Country,Description
            # print(f"{row['Nombre mostrado']}")


# Example usage
file_path_Odoo = "norm_files/exported_Odoo/Pedido de venta (sale.order) - SN.csv"
file_Zoho = "Sales_toImport.csv"
extract_info_from_csv(file_path_Odoo, file_Zoho)
