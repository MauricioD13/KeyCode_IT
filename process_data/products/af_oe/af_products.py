import csv
import sys
import json
import pandas as pd
def process_data(file_name):
    with open(file_name,"r") as file:
        reader = csv.DictReader(file)
        remotes_all = []
        list_remotes = []
        for row in reader:
            aux = row["Referencia interna"].split("-")
            try:
                remotes_all.append((aux[0],aux[1]))
            except:
                continue
            list_remotes.append(aux[0])

    return remotes_all, list_remotes
def process_data_sets(list_remotes: list) -> list:
    seen = set()
    duplicates = []
    for x in list_remotes:
        if x in seen:
            duplicates.append(x)
        else:
            seen.add(x)
    #print(duplicates)
    return duplicates

def remove_duplicates(duplicates: list, remotes_all: list) -> list:
    new_remotes = []
    for idx, remote_tuple in enumerate(remotes_all):
        if remote_tuple[0] not in duplicates and remote_tuple[1] == "AF":
            new_remotes.append(remote_tuple)
    return new_remotes

def save_in_csv(af_remotes: list, file_name:str):
    with open(file_name,"w") as file:
        write = csv.writer(file)
        write.writerows(af_remotes)



if __name__ == "__main__":
    remotes_all, list_remotes = process_data(sys.argv[1])
    duplicates = process_data_sets(list_remotes)
    af_remotes = remove_duplicates(duplicates, remotes_all)
    save_in_csv(sorted(af_remotes),sys.argv[2])

