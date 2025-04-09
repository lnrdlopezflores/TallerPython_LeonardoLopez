class hospital:
    def __init__(self):
        self.__NombrePaciente:str=''
        self.__Nss:int=1258
        self.__Enfermedad:str=''

    def getNombrePaciente(self)->str:
        return self.__NombrePaciente

    def getNss(self)->int:
        return self.__Nss

    @property
    def getEnfermedad(self)->str:
        return self.__Enfermedad

    def setNombrePaciente(self,nombre:str):
        self.NombrePaciente=nombre

    def setNss(self,nss:int):
        self.Nss=nss

    def setEnfermedad(self,enfermedad:str):
        self.Enfermedad=enfermedad

if __name__ == '__main__':
    hospital=hospital()

    hospital.__NombrePaciente='jose'

    print(hospital.getNombrePaciente())