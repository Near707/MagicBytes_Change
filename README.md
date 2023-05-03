# Cambiar los magicbytes de un archivo

Este es un programa de Python que te permite cambiar los magicbytes de un archivo para que sea un PNG, JPEG o GIF. El programa crea una copia del archivo original con un sufijo "-copy" en el nombre antes de modificarlo.

## Requisitos previos

Para ejecutar este programa, necesitarás tener instalado Python 3 en tu sistema operativo Linux.

## Uso

Para utilizar este programa, abre la terminal en Linux y navega hasta el directorio donde se encuentra el archivo `cambiar_magicbytes.py`. Luego, ejecuta el siguiente comando:

```
python3 cambiar_magicbytes.py archivo_original formato
```

En este comando, `archivo_original` es el nombre del archivo que deseas modificar y `formato` es el formato al que deseas convertir el archivo. El formato puede ser `png`, `jpeg` o `gif`. Asegúrate de escribir correctamente el nombre del archivo y el formato deseado, y de que el archivo original exista en el mismo directorio que el programa. La copia del archivo se creará en el mismo directorio con el sufijo "-copy" en el nombre.

## Ejemplo

Para convertir un archivo llamado `imagen.jpg` a un archivo PNG, ejecuta el siguiente comando:

```
python3 cambiar_magicbytes.py imagen.jpg png
```

Esto creará una copia del archivo original llamada `imagen.jpg-copy` y modificará la copia para cambiar los magicbytes al formato PNG.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de crear un pull request o reportar problemas en la sección de Issues.

## Licencia

Este programa está bajo la licencia MIT. Consulta el archivo LICENSE.md para más información.