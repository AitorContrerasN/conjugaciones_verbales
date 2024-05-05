import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_links(url):
    # Realiza la petición HTTP a la URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Busca todos los elementos 'a' dentro de los elementos con clase 'indexColumn'
    index_columns = soup.find_all(class_='indexColumn')
    
    # Extrae el texto y el href de cada enlace
    data = [(link.text, link.get('href')) for column in index_columns for link in column.find_all('a')]
    
    return data

def urls_to_dataframe(urls):
    # Lista para almacenar los datos de todas las URLs
    all_data = []
    
    # Itera sobre cada URL, extrae los enlaces y los añade a la lista de todos los datos
    for url in urls:
        links_data = extract_links(url)
        all_data.extend(links_data)
    
    # Crea un DataFrame con los datos
    df = pd.DataFrame(all_data, columns=['nombre', 'link'])
    
    return df

# Lista de URLs para analizar
urls = [
    'https://www.vocabulix.com/conjugacion2/a_spanish.html',
    'https://www.vocabulix.com/conjugacion2/h_spanish.html'
]

# Convierte los datos de las URLs en un DataFrame
df_links = urls_to_dataframe(urls)

# Muestra el DataFrame
print(df_links)
