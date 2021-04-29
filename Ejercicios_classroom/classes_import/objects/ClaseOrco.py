class Orco:
    

    def __init__(self, nombre, armadura, nivel, ataque, ojos = 2, piernas = 2, dientes = 56, salud = 100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

    def atacar(self, humano):
        humano.salud -= self.ataque - humano.armadura
        print("La vida del humano es: ", humano.salud)

    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def atributos(self):
        out = "Nombre:" + self.nombre + "\nArmadura: " + str(self.armadura) + "\nNivel:" + str(self.nivel) + "\nAtaque: " + str(self.ataque) + "\nOjos: " + str(self.ojos) + "\nPiernas:" + str(self.piernas) + "\nDientes: " + str(self.dientes) + "\nSalud:" + str(self.salud)
        return out



daniel = Orco(nombre = "daniel", armadura= 6, nivel = 40, ataque = 7)
print(daniel.nombre)
print(daniel.armadura)
print(daniel.nivel)
print(daniel.ataque)


print(daniel.atributos())

