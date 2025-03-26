def extraer(agenda:tuple):
    i:int=0
    while i<len(agenda):
        nombre, correo, telefono= agenda[i]
        i+=1
        yield nombre, correo, telefono


if __name__ == "__main__":
    agenda=[]
    agenda.append(('leonardo1', 'lnrd2324@gmail.com',  '2481369572'))
    agenda.append(('leonardo2', 'lnrd2334@gmail.com', '2481369573'))
    agenda.append(('leonardo3', 'lnrd2344@gmail.com', '2481369574'))
    agenda.append(('leonardo4', 'lnrd2354@gmail.com', '2481369575'))
    agenda.append(('leonardo5', 'lnrd2364@gmail.com', '2481369576'))
    agenda.append(('leonardo6', 'lnrd2374@gmail.com', '2481369577'))
    agenda.append(('leonardo7', 'lnrd2384@gmail.com', '2481369578'))
    agenda.append(('leonardo8', 'lnrd2394@gmail.com', '2481369570'))
    agenda.append(('leonardo9', 'lnrd2304@gmail.com', '2481369572'))
    agenda.append(('leonardo10', 'lnrd2314@gmail.com', '2481369532'))

    for a,b,c in extraer(agenda):
        print(f'valores: {a, b, c} ')