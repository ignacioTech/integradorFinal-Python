import sqlite3
inventario = {}
contador_index=1
#CREAR BASE DE DATOS Y LA TABLA DE PRODUCTOS.

def inicio_BBDD():
    conn = sqlite3.connect("C:\\Users\\Omar\\Documents\\GitHub\\integradorFinal-Python\\inventario.db")
    cursor= conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad    INTEGER NOT NULL CHECK(cantidad >= 0),
            precio  REAL NOT NULL CHECK(precio > 0),
            categoria TEXT
        )               
                   
    ''')
    
    conn.commit()
    conn.close()
    
# inicio_BBDD()

def mostrar_menu():
    print("")
    print("Gestion de Productos")
    print("")
    print("1- Registro: Ingreso de Productos")
    print("2- Visualización: Consulta de Productos")
    print("3- Actualizacion: Modificacion de Productos")
    print("4- Eliminacion: dar de baja un Producto")
    print("5- Listado: Listado completo de los productos de la base de datos")
    print("6- Reporte de Bajo Stock: Listado de productos con cantidad bajo mínimo")
    print("0- Salir")
    
def registrar_producto():
    
    print("\n Registro de producto nuevos")

    nombre = input("Ingrese el nombre del producto:").strip()
    descripcion = input("Ingrese la descripcion del producto:")
    
    #Validacion precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if(precio > 0):
                break
            print("El precio debe ser mayor o igual a 0")
        except ValueError:
            print("Entrada inválida, ingrese un valor mayor que cero")
            
     #Validacion cantidad
     
    while True:
        try:
            cantidad = float(input("Ingrese cantidad del producto: "))
            if(precio >= 0):
                break
            print("la cantidad debe ser mayor o igual a 0")
        except ValueError:
            print("Entrada inválida, ingrese un valor mayor o igual que cero")
    
    categoria = input("Ingrese la categoría del producto").strip()
    
    conn = sqlite3.connect("C:\\Users\\Omar\\Documents\\GitHub\\integradorFinal-Python\\inventario.db")
    cursor= conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTOO productos (
            codigo,
            nombre ,
            descripcion,
            cantidad ,
            precio ,
            categoria 
        )
        VALUES(NULL, ?,?,?,?,?)               
                   
    ''', (nombre, descripcion, cantidad, precio, categoria))
        id_producto =cursor.lastrowid
        codigo = f"PROD{id_producto}"
        
        cursor.execute(''' 
        UPDATE productos SET codigo = ? WHERE id = ? 
        ''', (codigo, id_producto))
        conn.commit()
        print(f"Registro exitoso, codigo asignado: {codigo}")
    
    except sqlite3.IntegrityError:
        print("No se pudo registrar")
    finally:
        conn.close()
        
def mostrar_productos():
    print("\n Listado de productos")

    if not inventario:
        print("El inventario se encuentra vacío")
    else:
        for codigo, datos in inventario.items():
            print(f"Codigo       : {codigo}")
            print(f"Nombre       : {datos["nombre"]}")
            print(f"descripcion  : {datos["descripcion"]}")
            print(f"cantidad     : {datos["cantidad"]}")
            print(f"precio       : {datos["precio"]}")
            print(f"categoria    : {datos["categoria"]}")
            print(f"- -"*50)
            
def actualizar_productos():
    print("\n Actualizacion de productos")
    codigo= input("Ingrese el código del producto a editar")

    if codigo in inventario:
        print(f"Producto encontrado: {inventario[codigo]["nombre"]}")
        print("Ingrese los nuevos datos o enter para no modificar")

        n_nombre=input("Ingrese el nuevo nombre")
        n_descripcion= input("Ingrese la nueva descripcion")
        
        #validacion de nueva cantidad
        while True :
            n_cantidad= input("ingrese la nueva cantidad").strip()
            if not n_cantidad :
                break
            try:
                n_cantidad = int(n_cantidad)
                if n_cantidad >= 0 :
                    break
                else:
                    print("ingreso invalido, debe ser numerico positivo")
            except ValueError:
                print("el valor debe ser positivo")
                
        
        #validacion de nuevo precio
        while True :
            n_precio= input("ingrese el nuevo precio").strip()
            if not n_precio :
                break
            try:
                n_precio = float(n_precio)
                if n_precio >= 0 :
                    break
                else:
                    print("ingreso invalido, debe ser numerico positivo")
            except ValueError:
                print("el valor debe ser positivo")
        
        n_categoria = input("Ingrese la nueva categoria")

        #Ãctualizar datos
        if n_nombre :
            inventario[codigo]["nombre"]= n_nombre
        if n_descripcion :
            inventario[codigo]["descripcion"]= n_descripcion
        if n_cantidad :
            inventario[codigo]["cantidad"]= n_cantidad
        if n_precio :
            inventario[codigo]["precio"]= n_precio
        if n_categoria :
            inventario[codigo]["categoria"]= n_categoria
            
        print("Producto actualizado")
    else:
        print("El codigo no existe")

def eliminar_producto():
    print("\n Eliminar Producto")
    codigo = input("Ingrese el codigo a eliminar").strip()

    if codigo in inventario:
        del inventario[codigo]
        print(f"El codigo: {codigo} , se ha eliminado")
    else:
        print(f"El codigo {codigo} no existe")

def buscar_producto():
    print("\n Buscar Producto")
    codigo = input("Ingrese el codigo a buscar").strip()

    if codigo in inventario:
        producto = inventario[codigo]
        print(f"\n Informacion del producto encontrado con el codigo{codigo}")

        print(f"Nombre       : {producto["nombre"]}")
        print(f"descripcion  : {producto["descripcion"]}")
        print(f"cantidad     : {producto["cantidad"]}")
        print(f"precio       : {producto["precio"]}")
        print(f"categoria    : {producto["categoria"]}")
            
    else:
        print(f"El codigo {codigo} no existe")
        

def reporte_bajo_stock():
    print("\n Reporte bajo stock")

    while True: 
        try:
            limite= int(input("Ingrese le limite de Stock para generar el reporte"))
            if limite >=0 :
                break
            else:
                print("Ingrese un numero positivo")
        except ValueError:
            print("Ingrese un numero positivo")
    
    print(f"\n productos con stock inferior a  {limite}")

    prod_bajo_stock=[
        (codigo, datos) for codigo, datos in inventario.items()
            if datos["cantidad"] <= limite
    ]
    
    if not prod_bajo_stock:
        print("No hay productos con bajo stock")
    
    for codigo, datos in prod_bajo_stock.items():
            print(f"Codigo       : {codigo}")
            print(f"Nombre       : {datos["nombre"]}")
            print(f"descripcion  : {datos["descripcion"]}")
            print(f"cantidad     : {datos["cantidad"]}")
            print(f"precio       : {datos["precio"]}")
            print(f"categoria    : {datos["categoria"]}")
            print(f"- -"*50)
        
#PROGRAMA PRINCIPAL

if __name__ == "__main__":
    inicio_BBDD()
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Ingrese una opción del 1 - 6 || 0(cero) para salir "))

            if opcion == 0:
                print("Salir")
                break

            elif opcion == 1:
                registrar_producto()

            elif opcion == 2:
                mostrar_productos()
                
            elif opcion == 3:
                print("3-Actualizacion-")
                actualizar_productos()
                
            elif opcion == 4:
                print("4-Eliminacion-")
                eliminar_producto()
                
            elif opcion == 5:
                print("5-Listado-")
                buscar_producto()
            elif opcion == 6:
                print("6-Reporte Bajo Stock-")
                reporte_bajo_stock()
            else:
                print("Ingrese un valor valido entre  1 - 6 || 0(cero) para salir ")
        except ValueError:
            print("ingrese un valor numerico valido")
    
    
    