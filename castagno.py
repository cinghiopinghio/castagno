from __future__ import division,print_function

class Pasta():
    def __init__(self,s):
        self.cod = s[0]
        self.cod_ean = s[1]
        self.cod_intra = s[2]
        self.descrizione = s[3][:40]
        self.pz = s[5]
        self.peso = s[6]
        self.prezzo = float(s[7].split()[1])
        self.iva = float(s[8].rstrip('%'))/100.0
        if s[9:13] != ['','','','']:
            self.cod5 = s[9]
            self.price5 = float(s[10].split()[1])
            self.cod25 = s[11]
            self.price25 = float(s[12].split()[1])
    def __str__(self):
        return self.cod+'\t'+self.descrizione
        
def read_file(filename):
    P={}
    with open(filename,'r') as fin:
        for line in fin:
            s = line.split(',')
            print (s)
            P[s[1]]=Pasta(s)
    return P

def main():
    P = read_file('2013.csv')

    for p in P:
        print (P[p])
    print (len(P))
    return 0

if __name__ == '__main__':
    main()
