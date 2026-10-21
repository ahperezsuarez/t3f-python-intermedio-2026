from tarea import cuentabancaria as cb

class CuentaAhorro(cb.CuentaBancaria):
    def __init__(self, nombre, cbu, saldo_inicial):
        super().__init__(nombre, cbu, saldo_inicial)
        self.tipo_de_cuenta = "Cuenta Ahorro"

    def extraer(self, monto):
        """Metodo extraer"""
        if (self.saldo - monto) < 0:
            raise ValueError("El saldo no puede ser negativo luego de la extraccion")
        self.saldo = self.saldo - monto
        print(f"Extraccion de ${monto} competada, su saldo es ${self.saldo}.")
              
    def aplicar_interes(self):
        interes = self.saldo * 0.001
        self.saldo += interes
        print(f"Se aplico el interes a su saldo ${interes}. Su saldo actual es ${self.saldo}.")
