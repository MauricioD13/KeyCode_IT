import csv
import sys
import json
import pandas as pd


def process_data(file_name):
    with open(file_name, "r") as file:
        excelFile = pd.read_excel(file_name)
        excelFile.to_csv("result.csv", index=None, header=True)
        dataFrame = pd.DataFrame(pd.read_csv("result.csv"))

    return dataFrame


def process_data_sets(list_remotes: list) -> list:
    seen = set()
    duplicates = []
    for x in list_remotes:
        if x in seen:
            duplicates.append(x)
        else:
            seen.add(x)
    # print(duplicates)
    return duplicates


def remove_duplicates(duplicates: list, remotes_all: list) -> list:
    new_remotes = []
    for idx, remote_tuple in enumerate(remotes_all):
        if remote_tuple[0] not in duplicates and remote_tuple[1] == "AF":
            new_remotes.append(remote_tuple)
    return new_remotes


def save_in_csv(af_remotes: list, file_name: str):
    with open(file_name, "w") as file:
        write = csv.writer(file)
        write.writerows(af_remotes)


if __name__ == "__main__":
    sales_orders = process_data(sys.argv[1])
    counter = 0
    """print(
        sales_orders[
            [
                "Referencia del pedido",
                "Comercial",
                "Cliente",
                "Pais",
                "Custom Note",
                "Estado",
            ]
        ]
    )"""
    for sale in sales_orders.index:
        if (
            sales_orders.loc[sale, "Estado"] == "Presupuesto"
            or sales_orders.loc[sale, "Custom Note"] == "<p><br></p>"
        ):
            sales_orders.drop(sale, inplace=True)
    print(sales_orders)
    # duplicates = process_data_sets(sales_orders)
    # af_remotes = remove_duplicates(duplicates, remotes_all)
    # save_in_csv(sorted(af_remotes), sys.argv[2])
