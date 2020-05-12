import os
import uuid
class Producto:

    listaProductos = []

    nombre = ""
    precio = 0
    cantidad = 0

    def __init__(self, codBarra, nombre, precio, cantidad):
        self.codBarra = codBarra
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def ingresaDatos():
        os.system('clear')
        codBarra = int(input("Código de barra: ")) #ingresa el codigo de barras
        nombre = input("Nombre: ") #ingresa el nombre
        precio = int(input("Precio: ")) #ingresa el precio
        cantidad = int(input("Cantidad: ")) #ingresa la cantidad
        instancia = str(uuid.uuid4)
        instancia = Producto(codBarra, nombre, precio, cantidad) #el codigo de barra se usa para instarciar el producto
        Producto.listaProductos.append(instancia.__dict__) #los atributos y sus valores son guardados en una lista
        os.system('clear')
    
    @classmethod
    def imprimirProductos(self):
        os.system('clear')
        print(*self.listaProductos, sep="\n")
        input("\nPresione cualquier tecla...")

    @classmethod
    def getProducto(self, i): return self.listaProductos[i]

    @classmethod
    def consultarStock(cls, nombreProducto):
        for i in range(len(Producto.listaProductos)): #recorre la lista de productos
            if Producto.listaProductos[i]['nombre'] == nombreProducto: #si encuentra el nombre del producto
                return Producto.listaProductos[i]['cantidad'] #devuelve el stock
    
    @classmethod
    def consultarPrecio(self, codBarra): #consulta el precio de un producto
        for i in range(len(self.listaProductos)): #recorre la lista de productos
            if self.listaProductos[i]['codBarra'] == codBarra: #si un codigo de barra coincide con el pasado
                return Producto.listaProductos[i]['precio'] #retorna el precio del producto con dicho codigo de barra

    @classmethod
    def indiceCodBarra(self, codBarra):
        for i in range(len(self.listaProductos)): #recorre la lista de productos
            if self.listaProductos[i]['codBarra'] == codBarra: #si un codigo de barra coincide con el pasado
                return i #retorna el indice del producto

    @classmethod
    def actualizacionDePrecio(self, codBarra, precio):
        i = self.indiceCodBarra(codBarra)
        self.listaProductos[i]['precio'] = precio