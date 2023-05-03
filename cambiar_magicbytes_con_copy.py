import argparse
import os
import shutil

# Funciones para cambiar los magicbytes a PNG, JPEG y GIF
def convertir_a_png(nombre_archivo):
    with open(nombre_archivo, 'r+b') as f:
        f.seek(0)
        f.write(b'\x89PNG\r\n\x1a\n')

def convertir_a_jpeg(nombre_archivo):
    with open(nombre_archivo, 'r+b') as f:
        f.seek(0)
        f.write(b'\xff\xd8\xff\xe0\x00\x10JFIF')

def convertir_a_gif(nombre_archivo):
    with open(nombre_archivo, 'r+b') as f:
        f.seek(0)
        f.write(b'GIF89a')

# Parsear argumentos de la línea de comandos
parser = argparse.ArgumentParser(description='Cambiar los magicbytes de un archivo a PNG, JPEG o GIF.')
parser.add_argument('archivo', metavar='archivo', type=str, help='nombre del archivo a convertir')
parser.add_argument('formato', metavar='formato', type=str, help='formato al que convertir el archivo', choices=['png', 'jpeg', 'gif'])
args = parser.parse_args()

# Verificar si el archivo existe
if not os.path.isfile(args.archivo):
    print('El archivo {} no existe.'.format(args.archivo))
    exit()

# Copiar el archivo original con un sufijo "-copy"
nombre_copia = args.archivo + '-copy'
shutil.copyfile(args.archivo, nombre_copia)

# Llamar a la función correspondiente según el formato seleccionado
if args.formato == 'png':
    convertir_a_png(nombre_copia)
    print('El archivo {} ha sido convertido a PNG.'.format(args.archivo))
elif args.formato == 'jpeg':
    convertir_a_jpeg(nombre_copia)
    print('El archivo {} ha sido convertido a JPEG.'.format(args.archivo))
elif args.formato == 'gif':
    convertir_a_gif(nombre_copia)
    print('El archivo {} ha sido convertido a GIF.'.format(args.archivo))
