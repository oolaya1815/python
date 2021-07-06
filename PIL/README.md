PIL es una biblioteca para Python, que proporciona al intérprete capacidades de edición de imágenes. 

Su instalación es muy sencilla:

```pip install Pillow```

El módulo ImageFilter contiene definiciones para un conjunto predefinido de filtros, que se pueden usar con el metodo Image.filter()

```PIL.ImageFilter.BoxBlur()```: desenfoca la imagen estableciendo cada píxel en el valor promedio de los píxeles en un cuadro cuadrado que extiende los píxeles de radio en cada dirección. 

```PIL.ImageFilter.FIND_EDGES()```: detección de bordes que se implementa mediante una convolución de un núcleo específico con la imagen

![img](https://github.com/oolaya1815/python/blob/main/PIL/PIL.PNG?raw=true)
