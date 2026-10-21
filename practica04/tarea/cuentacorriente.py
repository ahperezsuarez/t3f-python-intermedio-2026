from tarea import cuentabancaria as cb

class CuentaCorriente(cb.CuentaBancaria):
    def __init__(self, nombre, cbu, saldo_inicial, limite_descubierto = 500):
        super().__init__(nombre, cbu, saldo_inicial)
        self._limite_descubierto = limite_descubierto
        self.tipo_de_cuenta = "Cuenta Corriente"

    @property
    def limite_descubierto(self):
        return self._limite_descubierto
    
    @limite_descubierto.setter
    def limite_descubierto(self,limite_descubierto):
        if not isinstance(limite_descubierto,(int, float)):
            raise TypeError("Debe ingresar un numero.")
        if limite_descubierto < 0:
            raise ValueError("El limite descubierto no puede ser menor a 0 (cero)")
        self._limite_descubierto = limite_descubierto

    @cb.CuentaBancaria.saldo.setter
    def saldo(self, saldo):
        """Getter saldo personalizado"""
        if not isinstance(saldo, (int, float)):
            raise TypeError("El saldo debe ser un numero.")
        if (self._saldo + self.limite_descubierto) < 0:
            raise ValueError("El limite descubierto fue superado.")
        self._saldo = float(saldo)

    def extraer(self, monto):
        if (self.saldo + self.limite_descubierto) < monto:
            raise ValueError(f"La extraccion excede al limite descubierto.\nSaldo permitido: {(self.saldo + self.limite_descubierto)} | Extraccion: {monto}.")
        self.saldo -= monto
        print(f"Extraccion de ${monto} competada, su saldo es ${self.saldo} (descubierto de ${self.limite_descubierto}).")