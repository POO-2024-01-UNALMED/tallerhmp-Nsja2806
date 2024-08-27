from deportista import Deportista
from persona import Persona


class Futbolista:
    listaFutbolistas=[]

    def __init__(self,nombre, edad, altura, sexo, añospracticando, golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol",añospracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)

## Getters
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
## Setters
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados= golesMarcados
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas= tarjetasRojas
    
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil=piernaHabil

    def __str__(self):
        return f"Mi nombre es" + self.getNombre() + "soy profesional en el deporte" + self.getDeporte() + "tengo" + self.getEdad() + "años de edad y llevo" + self.getAñosParticipando() + "años en el deporte"