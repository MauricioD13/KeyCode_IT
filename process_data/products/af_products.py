import csv
import json
def process_data():
    with open("mandos.csv","r") as file:
        reader = csv.DictReader(file)
        counter = 0
        remotes = {}
        af_oe_remotes = []
        af_remotes = {}
        for row in reader:
            aux = row["Referencia interna"].split("-")
            if aux[0] in remotes:
                try:
                    af_remotes.pop(aux[0])
                except KeyError:
                    continue
                print(aux)
            if len(aux)>1 and aux[1] == "AF":
                remotes[aux[0]] = aux[1]
                af_remotes[aux[0]] = aux[1]
            else:
                af_oe_remotes.append(aux)

            #counter += 1
            if counter > 120:
                break
        print(json.dumps(remotes, indent=2))

if __name__ == "__main__":
    process_data()
