import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
from utils import filtrar_palabras, top_palabras

imparcial_url = "https://www.elimparcial.com/mexico/Ni-una-menos-Mujeres-se-manifiestan-contra-violencia-de-genero-20191125-0123.html"
telediario_url = "https://laguna.telediario.mx/nacional/hacen-pintas-y-destrozos-en-reforma-en-marcha-contra-violencia-de-genero"

excluido = [
    "la", "las", "el", "los", "de", "del", "se", "en", "y", "su", "a", "que", "por", "como", "para", "al",
    "17", "han", "lo", "con", "esta", "durante", "sobre", "algunas", "fueron", "tarde",
]

print("Obteniendo datos de las páginas...\n")

page_i = requests.get(imparcial_url)
page_t = requests.get(telediario_url)

print("Datos de las páginas obtenidos...\n")

#Se reestructura el texto en elementos entendibles de HTML para Python
soup_i = BeautifulSoup(page_i.content, "html.parser")
soup_t = BeautifulSoup(page_t.content, "html.parser")

'''
PARA IMPARCIAL
'''
#Ignoramos lo que no sea párrafo. Encuentra lo que sea noticia y párrafo
cuerpo_noticia_i =soup_i.find("div", class_="newsfull__body").find_all("p")
#print(cuerpo_noticia_i)

palabras_imparcial=filtrar_palabras(cuerpo_noticia_i,excluido)

#Se saca el top 15 de palabras
top_15_imparcial=top_palabras(palabras_imparcial,15)
# Graficar
plt.bar(top_15_imparcial.keys(), top_15_imparcial.values())
plt.show()

'''
PARA TELEDIARIO
'''
# Mantiene lo que está dentro del párrafo
cuerpo_noticia_t =soup_t.find("div", class_="field--text-paragraph").find_all("p")
palabras_telediario=filtrar_palabras(cuerpo_noticia_t,excluido)

# Top 15 de palabras
top_15_telediario=top_palabras(palabras_telediario,15)
#Graficar
plt.bar(top_15_telediario.keys(), top_15_telediario.values())
plt.show()
