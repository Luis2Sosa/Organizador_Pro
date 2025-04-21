# importamos los módulos
import os 
import shutil

# creamos el mensaje de bienvenida
print("---BIENVENIDO AL ORGANIZADOR DE ARCHIVOS---\n")

# Creamos la carpeta principal
carpeta_principal = "zona_1"

# creamos los archivos dentro de la carpeta
if not os.path.exists(carpeta_principal):
    os.mkdir(carpeta_principal)

with open(os.path.join(carpeta_principal, "archivo_vacio.txt"), "w") as a:
    pass
    
with open(os.path.join(carpeta_principal, "archivo_1.tmp"), "w") as a:
    a.write("Archivo de prueba 1")

with open(os.path.join(carpeta_principal, "archivo_2.txt"), "w") as a:
    a.write("Archivo de prueba 2")
    
with open(os.path.join(carpeta_principal, "archivo_3.pdf"), "w") as a:
    a.write("Archivo de prueba 3")
    
with open(os.path.join(carpeta_principal, "archivo_4.jpg"), "w") as a:
    a.write("Archivo de prueba 4")

# Recorremos los archivos    
for archivo in os.listdir(carpeta_principal):
    ruta = os.path.join(carpeta_principal, archivo)
    
    # Borramos si el archivo esta vacio o termina en .tmp
    if os.path.isfile(ruta) and (os.path.getsize(ruta) == 0 or archivo.endswith(".tmp")):
        os.remove(ruta)
        print(f"Eliminado: {archivo}")
    
    # Verificamos la extension del archivo
    if os.path.isfile(ruta) and "." in archivo:
        extension = archivo.split(".")[-1]
        ruta_1 = os.path.join(carpeta_principal, extension)
        
        # Creamos la carpeta si no existe
        if not os.path.exists(ruta_1):
            os.mkdir(ruta_1)
            
        # Movemos el archivo a esa carpeta    
        ruta_2 = os.path.join(ruta_1, archivo)
        shutil.move(ruta, ruta_2)
        print(f"{archivo} -> {extension}")
        
# Mensaje final        
print("Limpieza y organización completada con éxito")
        