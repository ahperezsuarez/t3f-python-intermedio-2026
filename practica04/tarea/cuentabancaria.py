"""Módulo para la gestión de cuentas bancarias."""
from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    """Inicializa los atributos de la cuenta bancaria."""
    def __init__(self, nombre, cbu, saldo_inicial):
        self.nombre = nombre
        self._cbu = cbu
        self._saldo = saldo_inicial
        self.tipo_de_cuenta = "Cuenta Bancaria"

    def __str__(self):
        return f"[{self.tipo_de_cuenta}] TITULAR: {self._nombre} | CBU: {self._cbu} | SALDO: ${self._saldo}.\n"

    @property
    def nombre(self):
        """Setter Nombre"""
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        """Getter Nombre"""
        if not isinstance(nombre, str):
            raise TypeError("Ingrese un nombre correcto.")
        self._nombre = nombre

    @property
    def cbu(self):
        """Setter CBU"""
        return self._cbu

    @property
    def saldo(self):
        """Setter saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        """Getter saldo"""
        if not isinstance(saldo, (int, float)):
            raise TypeError("El saldo debe ser un numero.")
        if saldo < 0:
            raise ValueError("No se permite saldo negativo.")
        self._saldo = float(saldo)

    @abstractmethod
    def extraer(self, monto):
        pass

    def depocitar(self, depocito):
        """Realiza el depocito de dinera a la cuenta"""
        if depocito <= 0:
            raise ValueError("El valor a depocitar debe ser mayor a 0 (cero). ")
        self._saldo = self._saldo + depocito
