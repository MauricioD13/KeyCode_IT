from bs4 import BeautifulSoup
import csv

with open("keys_data.html", "r") as file, open("key_data_parsed.csv","w") as file_parsed:

    html = file.read()
    soup = BeautifulSoup(html, "html.parser")
    csv_writer = csv.writer(file_parsed)
    row = []
    csv_writer.writerow(["Brand","Model","Year","VIN REF","Original Part","KEYDIY REF","Programming","Channel"])
    for line in soup.find_all("tr"):
        for line_td in line.find_all("td"):
            if line_td.string != None:
                row.append(line_td.string)
            else:
                row.append("None")
        csv_writer.writerow(row)
        row = []
    