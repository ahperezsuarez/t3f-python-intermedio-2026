from tarea import cuentaahorro as ca

def main():
    cuenta_bancaria = ca.CuentaAhorro("Carlos Rossi", "285001", saldo_inicial=1000)

    print(cuenta_bancaria)
    print("---extraccion---")
    cuenta_bancaria.extraer(100)
    print(cuenta_bancaria)
    print("---Interes---")
    cuenta_bancaria.aplicar_interes()
    print(cuenta_bancaria)

if __name__ == "__main__":
    main()
