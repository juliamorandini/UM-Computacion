class Cliente:
    def __init__(self, nombre, apellido, mail, dni, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail   
        self.dni = dni
        self.estado = estado

    #gets
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_mail(self):
        return self.mail
    
    def get_dni(self):
        return self.dni
    
    def get_estado(self):
        return self.estado
 
    #sets
    def set_mail(self, new_mail: str):
        self.mail = new_mail

    def set_estado(self, new_estado: str):
        self.estado = new_estado

    def set_nombre(self, new_nombre: str):
        self.nombre = new_nombre
    


class CuentaBancaria:
    def __init__(self, saldo, tipo_cuenta, movimientos, estado):
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.movimientos = movimientos
        self.estado = estado

    def ingresar(self, monto: float):
        if (monto > 0):
            self.saldo += monto

    def retirar(self, monto: float):
        if (monto>0 and monto <= self.saldo):
            self.saldo -= monto
    
    def mostrar_saldo(self):
        return self.saldo
    



    #gets
    def get_saldo(self):
        return self.saldo
    
    def get_tipo_cuenta(self):
        return self.tipo_cuenta
    
    def get_movimientos(self):
        return self.movimientos
    
    def get_estado(self):
        return self.estado
    
    #sets
    def set_saldo(self, new_saldo: float):
        self.saldo = new_saldo
    
    def set_tipo_cuenta(self, new_tipo_cuenta: str):
        self.tipo_cuenta = new_tipo_cuenta
    
    def set_movimientos(self, new_movimientos: list):
        self.movimientos = new_movimientos
    
    def set_estado(self, new_estado: str):
        self.estado = new_estado
    
