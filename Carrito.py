from Producto import Producto
import copy
import uuid
# import copy as copiar

class Carrito():

    listaCarrito = []
    listaBackUp = []

    @classmethod
    def agregarItem(self, codBarra, nuevaCantidad): #obtiene el codigo de barra y la cantidad
        i = Producto.indiceCodBarra(codBarra)
        self.listaBackUp = copy.deepcopy(Producto.listaProductos)
        self.listaCarrito.append(self.listaBackUp[i])
        self.listaCarrito[-1]['cantidad'] = nuevaCantidad

    @classmethod
    def eliminarItem(self, codigoBarra, nuevaCantidad):
        for i in range(len(self.listaCarrito)):
            if self.listaCarrito[i]['codBarra'] == codigoBarra:
                if self.listaCarrito[i]['codBarra'] >= nuevaCantidad:
                    self.listaCarrito[i]['cantidad'] -= nuevaCantidad
                else:
                    print("La cantidad a eliminar es mayor a la ingresada previamente.")
    
    @classmethod
    def imprimirCarrito(self): print(*self.listaCarrito, sep="\n") #imprime el carrito en forma de lista

    @classmethod
    def precioTotal(self):
        precio = 0
        for i in range(len(self.listaCarrito)):
            precio += self.listaCarrito[i]['precio'] * self.listaCarrito[i]['cantidad']
        print("Total de la compra: " + str(precio))

    @classmethod
    def actualizaStock(self):
        for i in range(len(self.listaCarrito)):
            for j in range(len(Producto.listaProductos)):
                if self.listaCarrito[i]['codBarra'] == Producto.listaProductos[j]['codBarra']:
                    Producto.listaProductos[j]['cantidad'] -= self.listaCarrito[i]['cantidad']