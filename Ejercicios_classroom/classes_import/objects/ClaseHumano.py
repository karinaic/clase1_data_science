
class Humano:
    pass

    def __init__(self, nombre, armadura, nivel, ataque, ojos =2, piernas = 2, dientes = 32,salud =100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

    def atacar(self, Orco):
        orco.salud -= self.ataque - orco.armadura
        print("La vida del orco es", orco.salud)

    def no_vivo(self):
        if self.salud <= 0:
            True
        else:
            False

    def atributos(self):
        out = "Nombre:" + self.name + "\nArmadura: " + str(self.armadura) + "\nNivel:" + str(self.nivel) + "Ataque: " + self.ataque + "\nOjos: " + str(self.ojos) + "\nPiernas:" + str(self.piernas) + "\nDientes: " + str(self.dientes) + "\nSalud:" + str(self.salud)
        return out