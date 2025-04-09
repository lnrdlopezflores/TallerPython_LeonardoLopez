class ListaDatos:

    def __init__(self,matricula:str,estudiante:str,asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura

if __name__=='__main__':
    lista=[]
    lista.append(ListaDatos('123451', 'juan carlos', 'sist-op'))
    lista.append(ListaDatos('123452', 'cecilia', 'LYA'))
    lista.append(ListaDatos('123453', 'federico', 'bd'))
    lista.append(ListaDatos('123454', 'paola', 'POO'))

    for obj in lista:
        print(f"matricula: {obj.matricula}")
        print(f"estudiane: {obj.estudiante}")
        print(f"asignatura: {obj.asignatura}")