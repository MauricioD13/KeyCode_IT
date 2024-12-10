import csv
from datetime import datetime, timedelta
import os

def marcar_fecha(fecha_str):
    fecha = datetime.strptime(fecha_str,'%Y-%m-%d')
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha
    if diferencia > timedelta(days=180):
        return 6, str(diferencia).split(",")[0]
    if diferencia > timedelta(days=90):
        return 3, str(diferencia).split(",")[0]
    return 0, str(diferencia).split(",")[0]

def buscar_ultimo_pedido():
    with open("Contactos_odoo.csv","r") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            if row["Nombre mostrado"] and row["URL de inicio de sesión"] and row['Pedido de venta/Última actualización el']:
                print("*****************************************************")
                
                marca = marcar_fecha(row['Pedido de venta/Última actualización el'].split(" ")[0])

def contactos_ultimo_pedido(clients_list: list):
    
    with open("Contactos_odoo.csv","r") as file, open("contactos_portal.csv","w") as outfile_accounts:        
        reader = csv.DictReader(file, delimiter=",")
        fieldnames = ['id_externa','Nombre cliente','Comercial','Ultima compra hace (dias)','Ultima compra hace mas de (meses)']
        writer = csv.DictWriter(
                outfile_accounts, fieldnames=fieldnames
            )
        writer.writeheader()
        count = 0
        print(reader.fieldnames)
        print(f"Lista de contactos: {len(clients_list)}")
        for row in reader:
            allow = False

            for client in clients_list:
                if row["Nombre mostrado"] in clients_list:
                    allow = True
                    clients_list.remove(row["Nombre mostrado"])
            
            if allow and row['Rango de proveedor'] == "0" and row['Pedido de venta/Última actualización el']:
                marca, diff = marcar_fecha(row['Pedido de venta/Última actualización el'].split(" ")[0])
                print(diff)
                if marca >= 6:
                    writer.writerow({
                        "id_externa":row['Identificación externa'],
                        "Nombre cliente":row['Nombre mostrado'],
                        "Comercial":row['Comercial'],
                        "Ultima compra hace (dias)": str(diff),
                        "Ultima compra hace mas de (meses)": marca    
                    })
                elif marca == 3:
                    writer.writerow({
                        "id_externa":row['Identificación externa'],
                        "Nombre cliente":row['Nombre mostrado'],
                        "Comercial":row['Comercial'],
                        "Ultima compra hace (dias)": str(diff),
                        "Ultima compra hace mas de (meses)": marca 
                    })
              
                count += 1
        print(f"Contador: {count}")

def usuarios_portal():
    if os.path.exists('Usuarios_SinAutenticar.csv') and os.path.exists('Usuarios_VigentesAuth.csv'):
        return False
    with open("Usuarios_res_users.csv","r") as file, open('Usuarios_SinAutenticar.csv','w') as output_file, open('Usuarios_VigentesAuth.csv','w') as output_file_auth:
        reader = csv.DictReader(file, delimiter=",")
        fieldnames = ['Nombre','Correo','Acceso al portal','Autenticacion hace (meses)']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        
        fieldnames_auth = ['Nombre','Correo']
        writer_auth = csv.DictWriter(output_file_auth, fieldnames=fieldnames_auth)
        #file_list = ['Usuarios_SinAutenticar.csv']
        counter_6 = 0
        counter_3 = 0
        counter_NN = 0
        counter = 0
        writer.writeheader()
        writer_auth.writeheader()
        clients_list = []
        for row in reader:
            try:
                marca, aux = marcar_fecha(row["Última autenticación"].split(" ")[0])
            except ValueError:
                marca = -1
            if row['Compartir usuario'] == 'True':
                
                if marca == 6:
                    writer.writerow({"Nombre": row['Nombre'],
                                     "Correo": row['Usuario'],
                                     "Acceso al portal": row['Compartir usuario'],
                                     "Autenticacion hace (meses)": marca})
                    clients_list.append(row['Nombre'])
                    counter_6 += 1
                elif marca == 3:
                    writer.writerow({"Nombre": row['Nombre'],
                                     "Correo": row['Usuario'],
                                     "Acceso al portal": row['Compartir usuario'],
                                     "Autenticacion hace (meses)": marca                 
                    })
                    counter_3 += 1
                    clients_list.append(row['Nombre'])
                    
                elif marca == -1:
                    writer.writerow({"Nombre": row['Nombre'],
                                     "Correo": row['Usuario'],
                                     "Acceso al portal": row['Compartir usuario'],
                                     "Autenticacion hace (meses)": "Nunca"
                    })
                    counter_NN += 1
                else:
                    writer_auth.writerow({"Nombre": row['Nombre'],
                                     "Correo": row['Usuario'],
                    })
                    counter +=1
        print(f"Cant. 6 meses: {counter_6}\nCant. 3 meses: {counter_3}")
        print(f"Cant. no autenticado: {counter_NN}\nCant. vigente: {counter}")
        print(f"Total: {counter_6+counter_3+counter+counter_NN}")
        return clients_list
if __name__ == "__main__":
    clients_list = usuarios_portal()
    contactos_ultimo_pedido(clients_list)