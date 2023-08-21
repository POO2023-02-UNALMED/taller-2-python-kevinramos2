class Asiento:
    def init(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
      
    def cambiarColor(self, color):
        if (color == 'amarillo' or color == 'verde' or color == 'rojo' or color == 'blanco' or color == 'negro'):
            self.color = color