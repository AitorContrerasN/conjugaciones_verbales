import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def extract_links(url):
    try:
        # Realiza la petición HTTP a la URL
        response = requests.get(url, timeout=10)  # Añadido timeout para manejar URLs que no responden
        if response.status_code != 200:
            print(f"Error al acceder a {url}: Código de estado {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return []
    
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Busca todos los elementos 'a' dentro de los elementos con clase 'indexColumn'
        index_columns = soup.find_all(class_='indexColumn')
        if not index_columns:
            print(f"No se encontraron elementos con clase 'indexColumn' en {url}")
            return []
        
        # Extrae el texto y el href de cada enlace
        data = [(link.text.strip(), link.get('href')) for column in index_columns for link in column.find_all('a')]
        if not data:
            print(f"No se encontraron enlaces en los elementos 'indexColumn' de {url}")
            return []
        
        return data
    except Exception as e:
        print(f"Error al procesar {url}: {e}")
        return []

def urls_to_dataframe(urls):
    # Lista para almacenar los datos de todas las URLs
    all_data = []
    
    # Itera sobre cada URL, extrae los enlaces y los añade a la lista de todos los datos
    for url in urls:
        print(f"Procesando {url}...")
        links_data = extract_links(url)
        all_data.extend(links_data)
        
        # Espera 50 segundos antes de procesar la próxima URL
        time.sleep(50)
    
    # Crea un DataFrame con los datos
    df = pd.DataFrame(all_data, columns=['nombre', 'link'])
    
    return df

# Lista de URLs para analizar
urls = [
    'https://www.vocabulix.com/conjugacion2/a_spanish.html',
    'https://www.vocabulix.com/conjugacion2/a1_spanish.html',
    'https://www.vocabulix.com/conjugacion2/a2_spanish.html',
    'https://www.vocabulix.com/conjugacion2/b_spanish.html',
    'https://www.vocabulix.com/conjugacion2/c_spanish.html',
    'https://www.vocabulix.com/conjugacion2/c1_spanish.html',
    'https://www.vocabulix.com/conjugacion2/d_spanish.html',
    'https://www.vocabulix.com/conjugacion2/d1_spanish.html',
    'https://www.vocabulix.com/conjugacion2/e_spanish.html',
    'https://www.vocabulix.com/conjugacion2/e1_spanish.html',
    'https://www.vocabulix.com/conjugacion2/f_spanish.html',
    'https://www.vocabulix.com/conjugacion2/g_spanish.html',
    'https://www.vocabulix.com/conjugacion2/h_spanish.html',
    'https://www.vocabulix.com/conjugacion2/i_spanish.html',
    'https://www.vocabulix.com/conjugacion2/j_spanish.html',
    'https://www.vocabulix.com/conjugacion2/k_spanish.html',
    'https://www.vocabulix.com/conjugacion2/l_spanish.html',
    'https://www.vocabulix.com/conjugacion2/m_spanish.html',
    'https://www.vocabulix.com/conjugacion2/n_spanish.html',
    'https://www.vocabulix.com/conjugacion2/o_spanish.html',
    'https://www.vocabulix.com/conjugacion2/p_spanish.html',
    'https://www.vocabulix.com/conjugacion2/p1_spanish.html',
    'https://www.vocabulix.com/conjugacion2/q_spanish.html',
    'https://www.vocabulix.com/conjugacion2/r_spanish.html',
    'https://www.vocabulix.com/conjugacion2/r1_spanish.html',
    'https://www.vocabulix.com/conjugacion2/s_spanish.html',
    'https://www.vocabulix.com/conjugacion2/t_spanish.html',
    'https://www.vocabulix.com/conjugacion2/u_spanish.html',
    'https://www.vocabulix.com/conjugacion2/v_spanish.html',
    'https://www.vocabulix.com/conjugacion2/w_spanish.html',
    'https://www.vocabulix.com/conjugacion2/x_spanish.html',
    'https://www.vocabulix.com/conjugacion2/y_spanish.html',
    'https://www.vocabulix.com/conjugacion2/z_spanish.html'
]

# Convierte los datos de las URLs en un DataFrame
df_links = urls_to_dataframe(urls)

# Exporta el DataFrame a un archivo Excel
excel_path = '/Users/aitor/Desktop/links.xlsx'
df_links.to_excel(excel_path, index=False)

print(f"El DataFrame ha sido exportado a {excel_path}")
