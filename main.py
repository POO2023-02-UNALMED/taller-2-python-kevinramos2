class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
      
    def cambiarColor(self, color):
        if color in  ['amarillo', ' verde', 'rojo', 'blanco', 'negro']:
            self.color = color

class Auto:
    cantidadCrados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCrados += 1

    def cantidadAsientos(self):
        totalAsientos = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                totalAsientos += 1
        return totalAsientos
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for pieza in self.registro:
                if (pieza.registro) != self.registro:
                    return ('Las piezas no son originales')
                else:
                    return ('Auto original')
        return ('Las piezas no son originales')

class Motor:
    def __init__(self, numerocilindro, tipo, registro):
        self.numeroCilindro = numerocilindro
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo in ['electrico', 'gasolina']:
            self.tipo = tipo 