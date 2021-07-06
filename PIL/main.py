''' Usando Python y PIL para procesamiento de imagenes'''           

#%% Cargando las librerias necesarias 
from PIL import Image, ImageFilter

#%% Ruta donde se encuentra nuestra imagen
path_image = 'image.png'

#%% Conversion a escala de grises
img = Image.open(path_image).convert('LA')
img.show()

#%% Filtro para desenfocar imagen
img = Image.open(path_image).filter(ImageFilter.BoxBlur(30))
img.show()

#%% Filtro para encontrar bordes 
img = Image.open(path_image).filter(ImageFilter.FIND_EDGES)
img.show()

#%% Filtro para contornos
img = Image.open(path_image).filter(ImageFilter.CONTOUR)
img.show()
