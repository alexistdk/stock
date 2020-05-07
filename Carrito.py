from Producto import Producto
import uuid

class Carrito():
    
    listaCarrito = []

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    @classmethod
    def agregarItem(self, codBarra, nuevaCantidad): #obtiene el codigo de barra y la cantidad
        pass
       
    @classmethod
    def eliminarItem(codigoBarra, cantidad):
        pass
    
    @staticmethod
    def imprimirCarrito():
        print(*Carrito.listaCarrito, sep="\n")