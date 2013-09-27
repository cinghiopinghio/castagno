import configparser

class Pasta():
    def __init__(self,s):
        self.cod = s[0]
        self.cod_ean = s[1]
        self.cod_intra = s[2]
        self.descrizione = s[3][:40]
        self.pz = int(s[5])
        self.peso = s[6]
        self.prezzo = float(s[7].split()[1])
        self.iva = float(s[8].rstrip('%'))/100.0
        if s[9:13] != ['','','','\n']:
            self.cod5 = s[9]
            self.price5 = float(s[10].split()[1])
            self.cod25 = s[11]
            self.price25 = float(s[12].split()[1])
    def __str__(self):
        return self.cod+'\t'+self.descrizione
class Ordini():
    def __init__(self,nome,ordine):
        self.nome = nome
        self.ordine = []
        for cod in ordine:
            self.ordine.append(Ordine(cod,ordine[cod]))
class Ordine():
    def __init__(self,cod,numero):
        self.cod = cod
        self.num = numero
    def __str__(self):
        return self.cod+' - {}'.format(self.num)

        
def read_file(filename):
    P={}
    with open(filename,'r') as fin:
        for line in fin:
            s = line.split(',')
            P[s[0]]=Pasta(s)
    return P

def leggi_ordini(filename):
    ordini = {}
    with open (filename,'r') as fin:
        for line in fin:
            line = line.split(':')
            if len(line) == 1:
                gente = line[0].strip()
                ordini[gente] = []
            else:
                cod = line[0].strip()
                num = int(line[1].strip())
                ordini[gente].append(Ordine(cod,num))

    return ordini


    p = []
    for gente in ordini.sections():
        print (gente)
        for codice in ordini[gente]:
            print (codice,ordini[gente][codice])
        p.append(Ordini(gente,ordini(gente)))
    return 0


def main():
    P = read_file('2013.csv')
    print (len(P),' tipi di roba')
    print (P['1PBSPA'])

    a = leggi_ordini('ordini.ini')
    for aa in a:
        print ('---',aa)
        for o in a[aa]:
            print (o, P[o.cod].prezzo*P[o.cod].pz)
    return 0

if __name__ == '__main__':
    main()
