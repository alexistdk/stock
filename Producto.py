import os

class Producto:

    listaProductos = []
    listaCodBarra = []

    nombre = ""
    precio = 0
    cantidad = 0

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def ingresaDatos():
        os.system('clear')
        codBarra = int(input("Código de barra: ")) #ingresa el codigo de barras
        Producto.listaCodBarra.append(codBarra)
        nombre = input("Nombre: ") #ingresa el nombre
        precio = int(input("Precio: ")) #ingresa el precio
        cantidad = int(input("Cantidad: ")) #ingresa la cantidad
        codBarra = Producto(nombre, precio, cantidad) #el codigo de barra se usa para instarciar el producto
        Producto.listaProductos.append(codBarra.__dict__) #los atributos y sus valores son guardados en una lista
        os.system('clear')
    
    @staticmethod
    def imprimirProductos():
        os.system('clear')
        print(*Producto.listaProductos, sep="\n")
        input("\nPresione cualquier tecla...")

    @classmethod
    def consultarStock(cls, nombreProducto):
        for i in range(len(Producto.listaProductos)): #recorre la lista de productos
            if Producto.listaProductos[i]['nombre'] == nombreProducto: #si encuentra el nombre del producto
                return Producto.listaProductos[i]['cantidad'] #devuelve el stock
    
    @classmethod
    def consultarPrecio(self, codBarra): #consulta el precio de un producto
        indice = self.indiceCodigoBarra(codBarra) #almacena el indice del codigo de barra
        return Producto.listaProductos[indice]['precio'] #retorna el precio del producto con dicho codigo de barra

    @classmethod
    def indiceCodigoBarra(self, codBarra): return self.listaCodBarra.index(codBarra) #retorna el indice del codigo de barra pasado