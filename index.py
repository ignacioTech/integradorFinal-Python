inventario = {}
contador_index=1

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
    global contador_index
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
            precio = float(input("Ingrese cantidad del producto: "))
            if(precio >= 0):
                break
            print("la cantidad debe ser mayor o igual a 0")
        except ValueError:
            print("Entrada inválida, ingrese un valor mayor o igual que cero")
    
    categoria = input("Ingrese la categoría del producto").strip()
