from unittest import TestCase
from Producto import *
from Carrito import *


class TestCarrito(TestCase):

    def test_agrega_item(self):
        Producto.crea_producto("nesquik", 123456, 140, 100)
        Carrito.agregar_item(123456, 20)
        lista = [{'cod_barra': 123, 'precio': 60, 'cantidad': 40},
                 {'cod_barra': 123456, 'precio': 140, 'cantidad': 20}]
        self.assertEqual(lista, Carrito.lista_carrito)

    def test_no_elimina_item(self):
        Carrito.eliminar_item(123456, 6)
        self.assertNotEqual(([{'cod_barra': 123456, 'precio': 140, 'cantidad': -1}]), Carrito.lista_carrito)

    def test_costo_compra(self):
        Carrito.eliminar_item(123456, 15)
        Carrito.eliminar_item(123, 40)
        self.assertEqual(700, Carrito.costo_compra())

    def test_eliminar_item(self):
        Carrito.eliminar_item(123456, 15)
        lista = [{'cod_barra': 123, 'precio': 60, 'cantidad': 0},
                 {'cod_barra': 123456, 'precio': 140, 'cantidad': 5}]
        self.assertEqual(lista, Carrito.lista_carrito)

    def test_actualiza_stock(self):
        Producto.crea_producto("leche", 123, 60, 50)
        Carrito.agregar_item(123, 40)
        Carrito.actualizar_stock()
        self.assertEqual([{'cod_barra': 123, 'precio': 60, 'cantidad': 10}], Producto.lista_productos)

    def test_confirma_compra(self):
        Carrito.confirmar_compra()
        self.assertEqual([], Carrito.lista_carrito)
