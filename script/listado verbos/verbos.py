import requests
from bs4 import BeautifulSoup

# URL de la página que quieres analizar
url = 'https://www.vocabulix.com/conjugacion2/a_spanish.html'

# Realizamos la petición HTTP a la URL
response = requests.get(url)

# Creamos la sopa con el contenido de la respuesta
soup = BeautifulSoup(response.content, 'html.parser')

# Buscamos todos los elementos que tengan la clase 'indexcolumn'
index_columns = soup.find_all(class_='indexColumn')

# Lista para almacenar los enlaces
links_list = []
text_list = []

# Recorremos cada elemento de indexcolumn encontrado
for column in index_columns:
    # Encontramos todos los enlaces dentro de este elemento
    links = column.find_all('a')
    # Recorremos cada enlace y extraemos el atributo 'href'
    for link in links:
        links_list.append(link.get('href'))
        text_list.append(link.text)

# Imprimimos la lista de enlaces
print(links_list)
print('---')
print(text_list)
