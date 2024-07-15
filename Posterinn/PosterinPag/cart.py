from django.contrib import messages

class carrito:
    def __init__(self,request ):
        self.request = request
        self.session = request.session

        carrito = self.session.get("carrito") # definimos la variable carrito 
        if not carrito: # si no existe la iniciamos con la session que tengamos abierta 
            carrito = self.session["caritto"] = {} # que sera un diccionario 

        self.carrito = carrito  # si existe se usa 

    def añadir_producto(self,producto):
        if producto.codigo not in self.carrito.keys(): # si no exitste el producto lo agrega al carrito
            self.carrito[producto.codigo]={
                "codigo":producto.codigo, 
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "categoria": str(producto.categoria),
                "cantidad" : 1,
                "total" : producto.precio,
                "stock" : producto.existencias,
                "descripcion" : producto.descripcion
            }
        else:   # si existe agrega + 1 a la cantidad noma
            for key, value in self.carrito.items(): 
                if key==producto.codigo and value["cantidad"] < producto.existencias: # si la cantidad es menor al stock 
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = producto.precio
                    value["total"]= int(value["total"]) + int(producto.precio)
                    
                    break
                else: # si es mayor a el stock
                    messages.success(self.request,"no mas existencias")
        self.guardar()    
        
    def guardar(self):
            self.session["carrito"] = self.carrito
            self.session.modified = True
     
    def quitar(self,producto):
        for key,value in self.carrito.items():
            if key == producto.codigo:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"]) - int(producto.precio)  
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break 
            
        self.guardar()

    


    
    def eliminar(self, producto):
        id =producto.codigo
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar()
    
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True