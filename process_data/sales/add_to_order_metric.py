import csv
import json
import sys

def create_customer(nombre):
    return {
        "nombre": nombre,
        "pedidos": 0,
    }

def main():
    with open("Sales_orders.csv","r") as file:
        reader = csv.DictReader(file)
        counter = 0
        previous_day = "0"
        previous_customer = ""
        customers = []
        customer ={
            "nombre": "",
            "pedidos": 0,
        }
        customers.append(customer)
        customer_add_order = []
        cash_on_delivery_orders = 0
        add_order = 0
        for row in reader:
            if row["Método entrega/Método entrega"] == "Agregar a Pedido":
                add_order += 1
                if row["Metodo de Pago"] == "Contrareembolso":
                    cash_on_delivery_orders += 1
                
            counter += 1
            if counter > int(sys.argv[1]):
                break
        #print(json.dumps(customer_add_order, indent=2))
        print(f"Muestra: {sys.argv[1]}")
        print(f"Cantidad de ordenes con 'agregar a pedido': {add_order}")
        print(f"Porcentaje de 'agregar a pedido': {add_order*100/int(sys.argv[1])} %")
        print(f"Cantidad de ordenes Contrareembolso con 'agregar a pedido': {cash_on_delivery_orders}")
        print(f"Porcentaje de 'agregar a pedido' con Contrareembolso: {cash_on_delivery_orders*100/int(sys.argv[1])} %")
        
            
            
            
if __name__ == "__main__":
    main()