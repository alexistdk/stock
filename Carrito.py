from Producto import Producto
import uuid
# import copy as copiar

class Carrito():
    
    codigoBarra = 0
    cantidad = 0

    listaCarrito = []

    def __init__(self, codigoBarra, cantidad):
        self.codigoBarra = codigoBarra
        self.cantidad = cantidad


    @classmethod
    def agregarItem(self, codBarra, nuevaCantidad): #obtiene el codigo de barra y la cantidad
        indice = Producto.indiceCodigoBarra(codBarra)
        self.listaCarrito.append(Producto.listaProductos[indice])
        self.listaCarrito[-1]['cantidad'] = nuevaCantidad

    @classmethod
    def eliminarItem(codigoBarra, cantidad):
        pass
    
    @classmethod
    def imprimirCarrito(self):
        print(*self.listaCarrito, sep="\n")

    @classmethod
    def precioTotal(self):
        precio = 0
        for i in range(len(self.listaCarrito)):
            precio += self.listaCarrito[i]['precio'] * self.listaCarrito[i]['cantidad']
        print("Total de la compra: " + str(precio))