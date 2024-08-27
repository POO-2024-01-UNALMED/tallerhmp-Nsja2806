class Deportista:
    def __init__(self, deporte="Futbol", añosPracticando=0):
        self._deporte=deporte
        self._añosPracticando=añosPracticando

## Getters
    def getDeporte(self):
        return self._deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
## Setters
    def setDeporte(self,deporte):
        self._deporte=deporte 

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando=añosPracticando
 
