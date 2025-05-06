from exceptions import MontoInsuficiente, MontoInvalido


class CuentaBancaria:
    def __init__(self, cliente, saldo, estado):
        self.cliente = cliente
        self.saldo = saldo
        self.estado = estado

    def obtener_saldo(self):
        return self.saldo

    def deposito(self, monto: float):
        if monto < 0:
            raise MontoInvalido()
        self.saldo += monto


class CajaAhorro(CuentaBancaria):
    def retiro(self, monto):
        if monto < 0:
            raise MontoInvalido()
        if monto > self.saldo:
            raise MontoInsuficiente()
        self.saldo -= monto


class CuentaCorriente(CuentaBancaria):
    def __init__(self, cliente, saldo, estado, limite_sobregiro):
        super().__init__(cliente, saldo, estado)
        self.limite_sobregiro = limite_sobregiro

    def retiro(self, monto):
        if monto < 0:
            raise MontoInvalido()
        if self.saldo + self.limite_sobregiro < monto:
            raise MontoInsuficiente()
        self.saldo -= monto
