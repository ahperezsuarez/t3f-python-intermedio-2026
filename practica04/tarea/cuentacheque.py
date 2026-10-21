from tarea import cuentabancaria as cb

class CuentaCheque(cb.CuentaBancaria):
    def __init__(self, nombre, cbu, saldo_inicial, costo_emision=50):
        super().__init__(nombre, cbu, saldo_inicial)
        self.tipo_de_cuenta = "Cuenta Cheque"
        self._costo_emision = costo_emision

    @property
    def costo_emision(self):
        return self._costo_emision
    
    @costo_emision.setter
    def costo_emision(self,costo_emision):
        if not isinstance(costo_emision,(int, float)):
            raise TypeError("Debe ingresar un numero.")
        if costo_emision < 0:
            raise ValueError("El costo de emision no puede ser menor a 0 (cero)")
        self._costo_emision = costo_emision

    def extraer(self, monto):
        if self._saldo < monto:
            raise ValueError("No se dispone de capital suficiente.")
        self._saldo -= (monto + self.costo_emision)
        print(f"Se emitio un cheque por ${monto}, su saldo actual es de ${self._saldo}. (comision fija de ${self.costo_emision})")