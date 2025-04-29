class Alumno:
    def __innit__ (self, legajo, nombre, email, estado):
        self.legajo = legajo
        self.nombre = nombre
        self.email = email
        self.estado = estado


    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def get_estado(self):
        return self.estado


# alumno_1 = Alumno( legajo = '64234', nombre = 'julia', email = 'j.morandini@um.edu.ar', estado = 'online')
# alumno_1.legajo = alumno_1.getlegajo() (todavia no esta pero esa es la idea )
