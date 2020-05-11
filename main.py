from Producto import Producto
from Carrito import Carrito
import os

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
        os.system('clear')
        menu()
    elif opcion == 3:
        consultarPrecio()
    elif opcion == 4:
        os.system('clear')
        consultarStock()
    elif opcion == 5:
        cobrar()
    else:
        print(Producto.listaCodBarra)

def agregarProducto(): #opcion 1
    Producto.ingresaDatos() #llama a la funcion ingresaDatos del objeto Producto
    agregarOtroProducto() #llama a la funcion de abajo para agregar más productos

def agregarOtroProducto(): #opcion 2
    respuesta = input("¿Desea agregar otro producto? S/N: ")
    if respuesta.casefold() == "s":
        agregarProducto()
    elif respuesta.casefold() == "n":
        os.system('clear')
        menu()
    else:
        respuestaInvalida()

def respuestaInvalida(): #opcion 2
    print("Respuesta inválida")
    agregarOtroProducto()

def consultarPrecio(): #opcion 3
    os.system('clear')
    codigo = int(input("Código de barra: "))
    precio = Producto.consultarPrecio(codigo)
    print("Precio: " + str(precio))
    input("\nPresione cualquier tecla...")
    os.system('clear')
    menu()    

def consultarStock(): #opcion 4
        producto = input("Nombre del producto: ")
        cantidadEnStock = Producto.consultarStock(producto)
        print("Cantidad en stock: " + str(cantidadEnStock))
        input("\nPresione cualquier tecla...")
        os.system('clear')
        menu()

def cobrar(): #opcion 5
    codigoBarra = int(input("Código de barra: "))
    while codigoBarra != 0:
        cantidad = int(input("Cantidad: "))
        Carrito.agregarItem(codigoBarra, cantidad)
        codigoBarra = int(input("Código de barra: "))
    Carrito.imprimirCarrito()
    Carrito.precioTotal()
    input("\nPresione cualquier tecla...")
    os.system('clear')
    menu()

menu()