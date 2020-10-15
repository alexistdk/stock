from unittest import TestCase
from Producto import *


class TestProducto(TestCase):

    def test_crea_productos(self):
        nesquik = Producto(123456, 140, 100)
        producto = Producto.crea_producto("nesquik", 123456, 140, 100)
        self.assertEqual(producto.__dict__, nesquik.__dict__)

    def test_consultar_stock_de_producto(self):
        Producto.crea_producto("queso_rallado", 124, 150, 40)
        self.assertEqual(40, Producto.consultar_stock_producto(124))

    def test_consultar_precio(self):
        Producto.crea_producto("nesquik", 123457, 120, 100)
        self.assertEqual(120, Producto.consultar_precio(123457))

    def test_actualizar_precio(self):
        Producto.crea_producto("azucar", 111, 75, 35)
        Producto.actualizar_precio(111, 80)
        self.assertEqual(80, Producto.consultar_precio(111))

    def test_indice_cod_barra(self):
        Producto.crea_producto("latte", 128, 90, 100)
        self.assertEqual(4, Producto.indice_cod_barra(128))

    def test_no_existe_producto(self):
        Producto.crea_producto("cafe", 13040, 90, 100)
        self.assertTrue(Producto.no_existe_producto(130))

    def test_existe_producto(self):
        Producto.crea_producto("latte", 128, 90, 100)
        self.assertFalse(Producto.no_existe_producto(128))
