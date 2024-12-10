import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import sys

START_HOUR = 9
END_HOUR = 17


def fix_date_hour(time_date):
    if time_date.hour < START_HOUR:
        return time_date.replace(hour=START_HOUR, minute=0, second=0)
    elif time_date.hour >= END_HOUR:
        next_day = time_date + timedelta(days=1)
        return next_day.replace(hour=START_HOUR, minute=0, second=0)
    else:
        return time_date


def first_word_of_string(carrier: str):
    if carrier:
        return carrier.split(" ")[0]
    else:
        return "vacio"


def create_csv(dataframe: pd.DataFrame, csv_filename: str):
    dataframe.to_csv(csv_filename)


def main():
    orders_df = pd.read_csv(sys.argv[1])

    # Prepare data
    orders_df["Fecha de traslado"] = pd.to_datetime(orders_df["Fecha de traslado"])
    orders_df["Fecha de creación"] = pd.to_datetime(orders_df["Fecha de creación"])
    orders_df["Transportista"] = orders_df["Transportista"].fillna("").str.strip()
    orders_df["Transportista_marca"] = orders_df["Transportista"].apply(
        first_word_of_string
    )
    orders_time_fix = orders_df["Fecha de creación"].apply(fix_date_hour)
    orders_df["Tiempo_albaran"] = orders_df["Fecha de traslado"] - orders_time_fix
    # Extract data from the main dataframe
    carrier_add_order = orders_df.loc[orders_df["Transportista"] == "Agregar a Pedido"]
    carriers_without_add_order = orders_df.loc[
        orders_df["Transportista"] != "Agregar a Pedido"
    ]
    carrier_stats = orders_df.groupby("Transportista_marca").count()
    customers_with_customs = orders_df.groupby("Contacto/Posición fiscal").count()
    orders_amount_by_customer = orders_df.groupby("Contacto").sum(
        "Pedido de venta/Importe a facturar"
    )
    orders_amount_by_taxing = orders_df.groupby("Contacto/Posición fiscal").sum(
        "Pedido de venta/Importe a facturar"
    )

    carrier_stats["Porcentaje"] = carrier_stats["Contacto"] / 50

    # Print info
    print(carriers_without_add_order["Tiempo_albaran"].describe())
    print(carrier_add_order["Tiempo_albaran"].describe())
    print(orders_df["Tiempo_albaran"].describe())
    print(carrier_stats)
    print(carrier_add_order)

    # Save info
    create_csv(orders_amount_by_taxing, "metricas_facturacion_aduana.csv")
    create_csv(orders_amount_by_customer, "metricas_facturacion_albaranes.csv")
    create_csv(carrier_stats, "metrica_transportistas.csv")
    create_csv(customers_with_customs, "metricas_clientes_aduana.csv")


if __name__ == "__main__":
    main()
