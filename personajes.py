
class Personaje:
    nombre = "default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("fuerza: ", self.fuerza)
        print("inteligencia: ", self.inteligencia)
        print("defensa: ", self.defensa)
        print("viada: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño,"puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.nombre, "es ", enemigo.vida)
        else:
            enemigo.morir()     

mi_Personaje = Personaje("paulo", 10, 1, 5, 10)
mi_enemigo = Personaje("enemy", 12, 34, 134, 45)
mi_Personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
