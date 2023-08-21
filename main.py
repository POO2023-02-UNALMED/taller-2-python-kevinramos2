class Asiento:
    def init(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
      
    def cambiarColor(self, color):
        if (color == 'amarillo' or color == 'verde' or color == 'rojo' or color == 'blanco' or color == 'negro'):
            self.color = color

class Auto:
    def init(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    cantidadCreados = 0

    def cantidadAsientos(self):
        totalAsientos = 0
        for asiento in self.asiento:
            if type(asiento) == Asiento:
                totalAsientos += 1
        return totalAsientos
        