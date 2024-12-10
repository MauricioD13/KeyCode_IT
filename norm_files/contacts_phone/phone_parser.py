import pandas as pd
import numpy as np
import re

# Diccionario de prefijos telefónicos por país (ampliado)
country_prefixes = {
    '1': '+1',  # Estados Unidos/Canadá
    '20': '+20',  # Egipto
    '30': '+30',  # Grecia
    '31': '+31',  # Países Bajos
    '32': '+32',  # Bélgica
    '33': '+33',  # Francia
    '34': '+34',  # España
    '36': '+36',  # Hungría
    '39': '+39',  # Italia
    '40': '+40',  # Rumania
    '44': '+44',  # Reino Unido
    '49': '+49',  # Alemania
    '52': '+52',  # México
    '55': '+55',  # Brasil
    '61': '+61',  # Australia
    '81': '+81',  # Japón
    '91': '+91',  # India
    '351': '+351',  # Portugal
    '358': '+358',  # Finlandia
    # Agregar más prefijos según sea necesario
}
country_prefixes_names = {
    'España': '34',
    'Francia': '33',
    'Senegal': '221',
    'Portugal': '351',
    'Reino Unido': '44',
    'República Democrática del Congo': '243',
    'Italia': '39',
    'Polonia': '48',
    'Suecia': '46',
    'Chipre': '357',
    'Australia': '61',
    'Grecia': '30'
}


# Función para normalizar los números de teléfono
def normalize_phone_number(phone_number, country, default_country_code='+34'):
    if pd.isna(phone_number):
        return phone_number
    # Eliminar caracteres no numéricos
    cleaned_number1 = re.sub(r'\D', '', phone_number)
    cleaned_number = cleaned_number1.replace(" "," ")
    cleaned_number = regex_func(cleaned_number)
    print(cleaned_number)
    #print(f"pre: {cleaned_number1} \t after: {cleaned_number}")
    # Revisar si el número ya tiene un prefijo conocido
    for name, country_code in country_prefixes_names.items():
        if country == name and cleaned_number[:len(country_code)] != country_code:
            return country_code + cleaned_number
    
    return cleaned_number
def regex_func(phone):
    #pattern = r'\b(\+?\d{1,3})?\s?(\(?\d{1,4}\)?)?\s?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b'
    pattern = r'\b(\+?\d{1,3}[\s-]?)?(\(?\d{1,4}\)?[\s-]?)?(\d{1,4}[\s-]?\d{1,4}[\s-]?\d{1,9})\b'
    matches = re.findall(pattern, phone)
    numbers_only = ""
    """for match in matches[0]:
        numbers_only = re.findall(r'\d+', match)"""
    numbers_only = [''.join(re.findall(r'\d+', match)) for match in matches[0]]
    
    return ''.join(numbers_only)

def main():
    # Leer el archivo CSV completo
    full_file_path = 'Contacto.csv'  # Cambia esto por la ruta a tu archivo
    full_df = pd.read_csv(full_file_path)
    new_phone = []
    for row in full_df.iterrows():
        new_phone.append(normalize_phone_number(row[1][2],row[1][6]))
    # Aplicar la normalización a todos los números de teléfono en la columna 'Mobile'
    #full_df['phone'] = full_df['phone'].apply(lambda x: normalize_phone_number(x))
    full_df['Teléfono'] = new_phone
    # Guardar el DataFrame con los números normalizados
    output_file_path = 'Contacto_normalized.csv'  # Cambia esto por la ruta donde quieres guardar el archivo
    full_df.to_csv(output_file_path, index=False)
    print("Process finished")


if __name__ == "__main__":
    main()