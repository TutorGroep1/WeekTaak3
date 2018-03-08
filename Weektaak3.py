def main():
    keuze = Bestand_kiezen()
    sequentie = bestand_lezen(keuze)
    lijst = splitten(sequentie)
    tellen(lijst)


def Bestand_kiezen():
    print("Welk bestand wil je gebruiken?")
    print("1: CDSHIV-1.txt \n2: CDSHIV-2.txt \n3: CDSSIV.txt\n4: CDSSIVmnd-2.txt")
    print("Of een bestand van een huishoudgen")
    print("5: E.coli-gen.fasta\n6: HomoSapiens-cds.txt\n7: Salmonella-gen.fasta\n8: Soybean-cds.txt")
    keuze = input("Welk bestand wil je openen")
    if keuze == '1':
        return 'CDSHIV-1.txt'
    elif keuze == '2':
        return 'CDSHIV-2.txt'
    elif keuze == '3':
        return 'CDSSIV.txt'
    elif keuze == '4':
        return 'CDSSIVmnd-2.txt'
    elif keuze == '5':
        return 'E.coli-gen.fasta'
    elif keuze == '6':
        return 'HomoSapiens-cds.txt'
    elif keuze == '7':
        return 'Salmonella-gen.fasta'
    elif keuze == '8':
        return 'Soybean-cds.txt'
    
def bestand_lezen(keuze):
    bestand = open(keuze)
    sequentie = ''
    for regel in bestand:
        regel = regel.replace("\n", "")
        if not regel.startswith(">"):
            sequentie += regel
    #print(sequentie)
    return sequentie

def splitten(sequentie):
    lijst = []
    for n in range(0,(len(sequentie)), 3):
        codon = sequentie[n:n+3]
        #print(codon)
        lijst.append(codon)
    #print(lijst)
    return lijst


def tellen(lijst):
    print("hoi")
    code = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
        'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
        'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
        'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
        'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
        'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
        'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
        'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
        'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
        'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
        'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
        'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 
        'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
        'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
        'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
        'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
       }
    count_code = {'TTT': 0, 'TCT': 0, 'TAT': 0, 'TGT': 0,
        'TTC': 0, 'TCC': 0, 'TAC': 0, 'TGC': 0,
        'TTA': 0, 'TCA': 0, 'TAA': 0, 'TGA': 0,
        'TTG': 0, 'TCG': 0, 'TAG': 0, 'TGG': 0,
        'CTT': 0, 'CCT': 0, 'CAT': 0, 'CGT': 0,
        'CTC': 0, 'CCC': 0, 'CAC': 0, 'CGC': 0,
        'CTA': 0, 'CCA': 0, 'CAA': 0, 'CGA': 0,
        'CTG': 0, 'CCG': 0, 'CAG': 0, 'CGG': 0,
        'ATT': 0, 'ACT': 0, 'AAT': 0, 'AGT': 0,
        'ATC': 0, 'ACC': 0, 'AAC': 0, 'AGC': 0,
        'ATA': 0, 'ACA': 0, 'AAA': 0, 'AGA': 0,
        'ATG': 0, 'ACG': 0, 'AAG': 0, 'AGG': 0, 
        'GTT': 0, 'GCT': 0, 'GAT': 0, 'GGT': 0,
        'GTC': 0, 'GCC': 0, 'GAC': 0, 'GGC': 0,
        'GTA': 0, 'GCA': 0, 'GAA': 0, 'GGA': 0,
        'GTG': 0, 'GCG': 0, 'GAG': 0, 'GGG': 0
       }


    for i in lijst:
        print(i)
        count_code[i] += 1
    print(count_code)
        


main()
