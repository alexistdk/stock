import os
from Carrito import *
from Producto import *


class Menu:

    @classmethod
    def menu_principal(cls):
        os.system('clear')
        opcion1 = "1. Agregar productos"
        opcion2 = "2. Consultar stock"
        opcion3 = "3. Consultar precio"
        opcion4 = "4. Cobrar"
        opcion5 = "5. Actualizar precios\n"
        opciones = [opcion1, opcion2, opcion3, opcion4, opcion5]
        for i in range(len(opciones)):
            print(opciones[i])
            pass
        opcion = int(input("Seleccione la opción: "))
        cls.seleccionar_opcion(opcion)
        pass

    @classmethod
    def seleccionar_opcion(cls, opcion):
        if opcion == 1:
            cls.agregar_producto()
            pass
        elif opcion == 2:
            cls.consultar_stock()
            pass
        elif opcion == 3:
            cls.consultar_precio()
            pass
        elif opcion == 4:
            cls.cobrar()
            pass
        elif opcion == 5:
            cls.actualizar_precio()
            pass
        else:
            print("Opción inválida")
            pass
        pass

    # arranca opción 1
    @classmethod
    def agregar_producto(cls):
        os.system('clear')
        Producto.ingresa_datos()
        cls.agregar_otro_producto()
        pass

    @classmethod
    def agregar_otro_producto(cls):
        respuesta = input("¿Desea agregar otro producto? S/N: ")
        if respuesta.casefold() == 's':
            cls.agregar_producto()
            pass
        elif respuesta.casefold() == 'n':
            system('clear')
            cls.menu_principal()
            pass
        else:
            cls.respuesta_invalida()
            cls.agregar_otro_producto()
            pass
        pass
    # termina opción 1

    @staticmethod
    def respuesta_invalida(): print("Respuesta inválida")

    # opción 2
    @classmethod
    def consultar_stock(cls):
        os.system('clear')
        cod_barra = int(input("Código de barra: "))
        cantidad = Producto.consultar_stock_producto(cod_barra)
        print("Cantidad en stock: " + str(cantidad))
        input("\nPresione cualquier tecla...")
        cls.menu_principal()
        pass

    # opcion 3
    @classmethod
    def consultar_precio(cls):
        os.system('clear')
        cod_barra = int(input("Código de barra: "))
        precio = Producto.consultar_precio(cod_barra)
        print("Precio: " + str(precio))
        input("\nPresione cualquier tecla...")
        cls.menu_principal()
        pass

    # opción 4
    @classmethod
    def cobrar(cls):
        os.system('clear')
        print("Cobrar\n")
        cod_barra = int(input("Código de barra: "))
        while cod_barra != 0:
            cantidad = int(input("Cantidad: "))
            Carrito.agregar_item(cod_barra, cantidad)
            system('clear')
            cod_barra = int(input("Código de barra: "))
        system('clear')
        cls.confirmar_eliminar_producto()
        pass

    @classmethod
    def confirmar_eliminar_producto(cls):
        confirmar = input("¿Desea eliminar algún producto? [S/N]: ")
        if confirmar.casefold() == 's':
            cod_barra = int(input("Código de barra: "))
            while cod_barra != 0:
                cantidad = int(input("Cantidad: "))
                Carrito.eliminar_item(cod_barra, cantidad)
                cls.confirmar_eliminar_producto()
        elif confirmar.casefold() == 'n':
            cls.cierra_compra()
        else:
            cls.respuesta_invalida()
            cls.confirmar_eliminar_producto()
        pass

    @classmethod
    def cierra_compra(cls):
        Carrito.imprimir_carrito()
        Carrito.costo_compra()
        Carrito.actualizar_stock()
        Carrito.confirmar_compra()
        input("\nPresione cualquier tecla...")
        cls.menu_principal()
        pass

    # opción 5
    @classmethod
    def actualizar_precio(cls):
        system('clear')
        print("Actualización de precio\n")
        cod_barra = int(input("Código de barra: "))
        precio = int(input("Precio: "))
        Producto.actualizar_precio(cod_barra, precio)
        cls.menu_principal()
        pass
