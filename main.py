from Producto import Producto
from Carrito import Carrito
import os

def menu():
    os.system('clear')
    print("1. Agregar productos\n"
          "2. Consultar stock\n"
          "3. Consultar precio\n"
          "4. Buscar producto\n"
          "5. Cobrar\n"
          "6. Actualizar precios\n")
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
    elif opcion == 6:
        actualizarPrecio()
    else:
        menu()

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
        agregarOtroProducto()

def respuestaInvalida(): print("Respuesta inválida")

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

def confirmarEliminarProducto(): #opcion 5
    confirmar = input("¿Desea eliminar algún producto?: ")
    if confirmar.casefold() == 's':
        codigoBarra = int(input("Código de barra: "))
        while codigoBarra != 0:
            cantidad = int(input("Cantidad: "))
            os.system('clear')
            Carrito.eliminarItem(codigoBarra, cantidad)
            confirmarEliminarProducto()
    elif confirmar.casefold() == 'n': 
        cierraCompra()
    else:
        respuestaInvalida()
        confirmarEliminarProducto()

def cierraCompra(): #opcion 5
    Carrito.imprimirCarrito()
    Carrito.precioTotal()
    Carrito.actualizaStock()
    input("\nPresione cualquier tecla...")
    del Carrito.listaBackUp[:]
    del Carrito.listaCarrito[:]
    os.system('clear')
    menu()

def cobrar(): #opcion 5
    os.system('clear')
    print("Cobrar\n")
    codigoBarra = int(input("Código de barra: ")) 
    while codigoBarra != 0:
        cantidad = int(input("Cantidad: "))
        Carrito.agregarItem(codigoBarra, cantidad)
        os.system('clear')
        codigoBarra = int(input("Código de barra: "))
    os.system('clear')
    confirmarEliminarProducto()

def actualizarPrecio(): #opcion 6
    os.system('clear')
    print("Actualización de precio\n")
    codBarra = int(input("Código de barra: "))
    precio = int(input("Precio nuevo: "))
    Producto.actualizacionDePrecio(codBarra, precio)
    menu()

menu()