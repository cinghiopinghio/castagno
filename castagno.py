
class Pasta():
    def __init__(self,s):
        self.cod = s[0].strip('"')
        self.cod_ean = s[1]
        self.cod_intra = s[2]
        self.descrizione = s[3]#[:40]
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
class Ordine():
    def __init__(self,cod,numero):
        self.cod = cod
        self.num = numero
    def totale(self,P):
        return prezzo (self.cod,P)
        #return P[self.cod].prezzo * P[self.cod].pz * (1+P[self.cod].iva)
    def __str__(self):
        return self.cod+' - {}'.format(self.num)
        
def prezzo (cod,P,num=None):
    prezzo_pacco = P[cod].prezzo * P[cod].pz * (1+P[cod].iva)
    if num is not None:
        prezzo_pacco *= num
    return prezzo_pacco

def read_file(filename):
    P={}
    with open(filename,'r') as fin:
        for line in fin:
            s = line.split(',')
            P[s[0].strip('"')]=Pasta(s)
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

    ordi = leggi_ordini('ordini.ini')
    totali = {}
    paste = {}
    for gente in ordi:
        print ('---',gente)
        tot = 0
        for pasta in ordi[gente]:
            par_tot = pasta.totale(P)
            print ('{0:12s} - {1:12.2f}'.format(pasta, par_tot))
            tot += par_tot
            if pasta not in paste:
                paste[pasta.cod] = pasta.num
            else:
                paste[pasta.cod] += pasta.num
        totali[gente] = tot
        print ('totale {0:25s}= {1:8.2f}'.format(gente,tot))

    print ('\nOrdine Totale:')
    for pasta in paste.keys():
        prz = prezzo(pasta,P,num=paste[pasta])
        print ('{0:12s} num {1:3d} prezzo {2:6.2f}'.format(pasta,\
                                                         paste[pasta],\
                                                         prz))
    print ('\nSpesa Totale = {0:12.2f}'.format(sum(totali.values())))
    return 0

if __name__ == '__main__':
    main()
