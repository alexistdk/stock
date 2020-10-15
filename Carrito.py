from Producto import *
from copy import deepcopy


class Carrito:
    lista_carrito = []
    lista_back_up = []

    @classmethod
    def agregar_item(cls, cod_barra, nueva_cantidad):
        i = Producto.indice_cod_barra(cod_barra)
        cls.lista_back_up = deepcopy(Producto.lista_productos)
        cls.lista_carrito.append(cls.lista_back_up[i])
        cls.lista_carrito[-1]['cantidad'] = nueva_cantidad
    pass

    @classmethod
    def eliminar_item(cls, cod_barra, nueva_cantidad):
        for i in range(len(cls.lista_carrito)):
            if cls.lista_carrito[i]['cod_barra'] == cod_barra:
                if cls.lista_carrito[i]['cantidad'] >= nueva_cantidad:
                    cls.lista_carrito[i]['cantidad'] -= nueva_cantidad
    pass

    @classmethod
    def imprimir_carrito(cls):
        print(*cls.lista_carrito, sep="\n")
        print("Total: " + str(cls.costo_compra()))

    @classmethod
    def costo_compra(cls):
        precio = 0
        for i in range(len(cls.lista_carrito)):
            precio += cls.lista_carrito[i]['precio'] * cls.lista_carrito[i]['cantidad']
        return precio

    @classmethod
    def actualizar_stock(cls):
        for i in range(len(cls.lista_carrito)):
            for j in range(len(Producto.lista_productos)):
                if cls.lista_carrito[i]['cod_barra'] == Producto.lista_productos[j]['cod_barra']:
                    Producto.lista_productos[j]['cantidad'] -= cls.lista_carrito[i]['cantidad']
    pass

    @classmethod
    def confirmar_compra(cls): cls.lista_carrito = []
