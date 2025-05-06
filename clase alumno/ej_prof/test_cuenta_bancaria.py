import unittest
from cuenta_bancaria import CuentaBancaria, CajaAhorro, CuentaCorriente
from exceptions import MontoInsuficiente, MontoInvalido


class TestCajaAhorro(unittest.TestCase):
    def test_obtener_saldo(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CajaAhorro(
            cliente=cliente,
            saldo=saldo,
            estado=estado,
        )

        # ejecución
        saldo = cuenta_bancaria.obtener_saldo()

        self.assertEqual(saldo, 0)

    def test_depositar(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CajaAhorro(
            cliente=cliente,
            saldo=saldo,
            estado=estado,
        )
        monto_a_ingresar = 100

        # ejecución
        cuenta_bancaria.deposito(monto=monto_a_ingresar)

        # assertar
        saldo_actual = cuenta_bancaria.obtener_saldo()
        self.assertEqual(saldo_actual, 100)

    def test_no_es_posible_retirar(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CajaAhorro(
            cliente=cliente,
            saldo=saldo,
            estado=estado,
        )
        monto_a_retirar = 100

        # ejecución
        with self.assertRaises(MontoInsuficiente):
            cuenta_bancaria.retiro(monto=monto_a_retirar)

    def test_es_posible_retirar(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CajaAhorro(
            cliente=cliente,
            saldo=saldo,
            estado=estado,
        )
        cuenta_bancaria.deposito(50000)
        monto_a_retirar = 5000

        # ejecución
        cuenta_bancaria.retiro(monto=monto_a_retirar)

        saldo = cuenta_bancaria.obtener_saldo()
        self.assertEqual(saldo, 45000)


class TestCuentaCorriente(unittest.TestCase):
    def test_no_es_posible_retirar(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CuentaCorriente(
            cliente=cliente,
            saldo=saldo,
            estado=estado,
            limite_sobregiro=500,
        )
        monto_a_retirar = 600

        # ejecución
        with self.assertRaises(MontoInsuficiente):
            cuenta_bancaria.retiro(monto=monto_a_retirar)

    def test_es_posible_retirar(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CuentaCorriente(
            cliente=cliente, saldo=saldo, estado=estado, limite_sobregiro=5000
        )
        monto_a_retirar = 5000

        # ejecución
        cuenta_bancaria.retiro(monto=monto_a_retirar)

        saldo = cuenta_bancaria.obtener_saldo()
        self.assertEqual(saldo, -5000)

    def test_depositar(self):
        # precondiciones
        cliente = "Juan Perez"
        saldo = 0
        estado = "activo"
        cuenta_bancaria = CuentaCorriente(
            cliente=cliente, saldo=saldo, estado=estado, limite_sobregiro=200
        )
        monto_a_ingresar = 100

        cuenta_bancaria.deposito(monto_a_ingresar)

        saldo = cuenta_bancaria.obtener_saldo()
        self.assertEqual(saldo, 100)
