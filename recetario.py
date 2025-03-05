import os
from pathlib import Path
from os import system


#Menu inicio

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
        
    return contador


def inicio():
    system('clear')
    print('*' * 50)
    print('5' * 5 + " Bienvenido al administrador de recetas " + 5 * '*')
    print('*' * 50)
    print('/n')
    print(f"Las recetas es en cuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)} ")
    
    elecion_menu = 'x'
    while not elecion_menu.isnumeric() or int(elecion_menu) not in range(1, 7):
        print("Elige una opcion:")
        print('''
           [1] - Leer receta
           [2] - Crear receta nueva
           [3] - Crear categoria nueva
           [4] - Eliminar receta
           [5] - Eliminar categoria
           [6] - Salir del programa''')
        elecion_menu = input()
        return (elecion_menu)

def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
        
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")
        
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'
    
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")
    
    return lista[int(eleccion_receta) -1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento esa receta ya existe")

def crear_categoria(ruta):
    existe = False
    
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu receta {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento esa receta ya existe")
            
            
if menu == 1:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mis_recetas)
    leer_receta(mi_receta)
    
    pass
elif menu == 2:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    

    
    pass
elif menu == 3:
    
    
    pass

elif menu == 4:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mis_recetas)
    
    pass
elif menu == 5:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    
    
    pass
elif menu == 6:
    # finalizar programa
    pass
