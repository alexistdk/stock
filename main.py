from Producto import Producto
from Carrito import Carrito

def menu():
    print("1. Agregar productos\n"
          "2. Consultar stock\n"
          "3. Consultar precio\n"
          "4. Buscar producto\n"
          "5. Cobrar\n")
    opcion = int(input("Seleccione la opcion: "))
    seleccionarOpcion(opcion)

def seleccionarOpcion(opcion):
    if opcion == 1:
        agregarProducto()
    elif opcion == 2:
        Producto.imprimirProductos()
        menu()
    elif opcion == 3:
        consultarPrecio()
    elif opcion == 4:
        consultarStock()
    elif opcion == 5:
        cobrar()
    else:
        print(Producto.listaCodBarra)

def agregarProducto(): #opcion 1
    Producto.ingresaDatos() #llama a la funcion ingresaDatos del objeto Producto
    agregarOtroProducto() #llama a la funcion de abajo para agregar más productos

def agregarOtroProducto():
    respuesta = input("¿Desea agregar otro producto? S/N: ")
    if respuesta.casefold() == "s":
        agregarProducto()
    elif respuesta.casefold() == "n":
        menu()
    else:
        respuestaInvalida()

def respuestaInvalida():
    print("Respuesta inválida")
    agregarOtroProducto()

def consultarPrecio(): #opcion 3
    codigo = int(input("Código de barra: "))
    precio = Producto.consultarPrecio(codigo)
    print("Precio: " + str(precio))
    menu()    

def consultarStock(): #opcion 4
        producto = input("Nombre del producto: ")
        cantidadEnStock = Producto.consultarStock(producto)
        print("Cantidad en stock: " + str(cantidadEnStock))
        menu()

def cobrar(): #opcion 5
    codigoBarra = int(input("Código de barra: "))
    while codigoBarra != 0:
        cantidad = int(input("Cantidad: "))
        Carrito.agregarItem(codigoBarra, cantidad)
        codigoBarra = int(input("Código de barra: "))
    Carrito.imprimirCarrito()

menu()