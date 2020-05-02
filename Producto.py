import uuid

class Producto:

    listaProductos = []
    listaID = []
    listaVentas = []

    def __init__(self, codigoBarra, nombre, precio, cantidad):
        self.codigoBarra = codigoBarra
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def ingresaDatos():
        codBarra = int(input("Código de barra: ")) #ingresa el codigo de barras
        nombre = input("Nombre: ") #ingresa el nombre
        precio = int(input("Precio: ")) #ingresa el precio
        cantidad = int(input("Cantidad: ")) #ingresa la cantidad
        nombreRandom = str(uuid.uuid4()) #genera un nombre random para la instancia
        nombreRandom = Producto(codBarra, nombre, precio, cantidad) #ese nombre se utiliza para generar un objeto
        Producto.listaProductos.append(nombreRandom.__dict__) #el objeto es almacenado en una lista
        Producto.listaID.append(nombreRandom) #almacena el nombre de las instancias en una lista
    
    @staticmethod
    def imprimirProductos():
        print(Producto.listaProductos)
    
    @classmethod
    def consultarStock(cls, nombreProducto): #se le ingresa el nombre de un producto
        for i in range(len(Producto.listaID)): #recorre la lista con el nombre de las instancias de los productos
            nombreObjeto = Producto.listaID[i] #se le asigna una variable a cada ID para poder revisarlo uno por uno
            if nombreObjeto.nombre == nombreProducto: #si el atributo nombre coincide con el producto
                cantidadEnStock = nombreObjeto.cantidad #almacena la cantidad de stock que tiene dicho objeto
        return cantidadEnStock #retorna la cantidad en stock que tiene
    
    @classmethod
    def consultarPrecio(cls, codigoBarra): #consulta el precio de un producto
        for i in range(len(Producto.listaID)): #recorre el vector con los id
            nombreObjeto = Producto.listaID[i] #se le asigna una variable a cada ID para poder revisarlo uno por uno
            if nombreObjeto.codigoBarra == codigoBarra: #si el atributo codigoBarra coincide con el codigo de barra
                precioDelProducto = nombreObjeto.precio #almacena el precio que tiene dicho objeto
        return precioDelProducto #retorna el precio

    @classmethod
    def venta(cls, codigoBarra, cantidad):
        for i in range(len(Producto.listaID)):
            nombreObjeto = Producto.listaID[i]
            if nombreObjeto.codigoBarra == codigoBarra:
                Producto.listaVentas.append(nombreObjeto.codigoBarra)
                Producto.listaVentas.append(cantidad)
        
    @classmethod
    def buscarCodBarra(cls, codigoBarra): #busca el codigo de barra
        for i in range(len(Producto.listaID)): #recorre la lista de ids
            nombreObjeto = Producto.listaID[i] #a cada id le asigna una variable
            if nombreObjeto.codigoBarra == codigoBarra: #si id.codBarra es igual al codigo de barra ingresado
                return nombreObjeto.codigoBarra #retorna el id

    @staticmethod
    def buscarIDporCodBarra(codBarra):
        for i in range(len(Producto.listaID)): #recorre la lista de ids
            instancia = Producto.listaID[i] #le asigna una variable a cada id
            if instancia.codigoBarra == codBarra: #si el codigo de barras del id coincide con el codigo pasado
                print(instancia) #no retorna el id

    @staticmethod #ToDo
    def mostrarCarrito(cls, codigoBarra):
        pass