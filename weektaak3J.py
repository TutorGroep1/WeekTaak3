import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def main():                                         #creeer de main functie, deze functie roept alle andere fucnties aan
    doorgaan = 'y'                                  #geef doorgaan basiswaarde y
    while doorgaan == 'y':                          #zo lang doorgaan waarde y heeft...
        filename = kiesBestand()                    #roep de kiesBestandfucntie aan en verkrijg hieruit de waarde filenaam
        if filename != 'fout':                      #als de kiesBestand functie niet 'fout' heeft gereturned...
            seqs = maakLijst(filename)              #roep de maakLijst functie aan en geef filenaam mee, verkrijg uit deze functie een lijst met sequenties (seqs)
            x = 0                                   #zet x op 0
            for i in seqs:                          #loop door de lijst met sequenties
                passSeq = seqs[x]                   #geef passSeq de waarde van de sequentie op de possitie van waarde x
                codonLijst = knipSeq(passSeq)       #roep de knipSeq functie aan en geef passSeq mee, verkrijg uit deze functie een lijst met 
                gebLijst = tellen(codonLijst)       #roep de tellen functie aan en geef codonLijst mee, verkrijg uit deze functie een lijst met het codongebruik
                dataLijst = dataSet(gebLijst)       #roep de dataSet functie aan en geef gebLijst mee, verkrijg uit deze functie een 
                plotten(dataLijst)                  #roep de plotten fucntie aan en geef dataLijst mee
                x+=1                                #verhoog x met 1
                
        print('-'*80, '\n') 
        doorgaan = input('wil je doorgaan? y/n ')   #vraag of de gebruiker nog een bestand wil inladen   
        print('\n', '-'*80)

        
def kiesBestand():                                                                  #creeer de kiesBestand fucntie, deze functie vraagt de gebruiker van welk bestand data moet wordenweergeven
    bestanden = ['CDSHIV-2.txt', 'CDSSIV.txt', 'CDSSIVmnd-2.txt', 'E.coli-gen.fasta', 'HIV1-env.txt', 'HIV1-IVG.txt', 'hiv2-glycoprotein.txt', 'HomoSapiens-cds.txt', 'Salmonella-gen.fasta', 'SIV-gp.txt', 'SIVmnd2-gp.txt', 'Soybean-cds.txt']
    print('je kan kiezen uit deze bestanden: \n')
    x=0                                                                             #geef x waarde 0
    for i in bestanden:                                                             #loop door de bestanden lijst
        print(x+1, ': ', bestanden[x])  
        x+=1                                                                        #verhoog x met 1
    try:                                                                            #probeer...
        keuze = int(input('welke van deze bestanden wil je openen? :'))             #geef keuze de waarde die de gebruiker invoert
    except ValueError:                                                              #als de invoer geen integer is
        print('dat is geen geldige invoer')                                         
        return 'fout'                                                               #return 'fout' zodat de fucntie opnieuw wordt gestart
    if keuze not in range(len(bestanden)+1):                                        #als de keuze buiten de beschikbare bestanden valt...
        print('dat is geen geldige invoer')
        return 'fout'                                                               #return 'fout' zodat de fucntie opnieuw wordt gestart
    else:                                                                           #anders...
        return bestanden[keuze-1]                                                   #return de naam van het gekozen bestand

    
def maakLijst(filename):                    #creeer de maakLijst fucntie, deze functie plakt losse stukken sequentie aan elkaar en zet deze in een lijst
    try:                                    #probeer...                                  
        file = open(filename)                 
    except FileNotFoundError:               #als het bestand niet bestaat
        print('dit bestand bestaat niet')
        quit()                              #stop 
    headers = []                            #maak een lege lijst voor headers
    seqs = []                               #maak een lege lijst voor de sequenties

    completeSeq = ''                        #maak een string voor een complete sequentie
    eerste = 0                              #geef eerste de waarde 0
    for line in file.readlines():           #lees het bestand...
        if line[0] == '>':                  #als het eerste teken van een line > is...
            line.rstrip()                   #strip de line
            headers.append(line)            #voeg deze line toe aan de headers lijst 
            if eerste != 0:                 #als eerste niet 0 is...
                seqs.append(completeSeq)    #voeg de waarde van de huidige sequentie toe aan de sequentielijst
                completeSeq = ''            #maak de sequentiestring weer leeg
            eerste+=1                       #verhoog eerste met 1
        else:                               #anders...
            line = line.rstrip()            #strip de line
            completeSeq+= line              #voeg de line toe aan de seq string
    seqs.append(completeSeq)                #voeg de line toe aan de sequentielijst
    return seqs                             #return de lijst met sequenties


def knipSeq(passSeq):                   #creeer de knipSeq fucntie, deze functie deelt sequenties op in stukjes van 3 
    codonLen = 0                        #zet codonLen op 0
    codon = ''                          #maak eenlege string in codon
    codonLijst = []                     #maak een lege lijst genaamd codonLijst om te vullen met de stukjes
    for i in passSeq:                   #loop door de gepasste sequentie...
        if codonLen == 3:               #als de lengte van het geknipte stuk 3 is
            codonLijst.append(codon)    #voeg het stukje toe aan  codonLijst
            codonLen = 0                #zet de lengte van het stukje op 0
            codon = ''                  #maak de codon leeg
            codon = codon + i           #voeg een nieuwe letter toe
            codonLen+=1                 #verhoog de lengte met 1
        else:                           #anders...
            codon = codon + i           #voeg een nieuwe leter toe
            codonLen+=1                 #verhoog de lengte met 1
    codonLijst.append(codon)            #voeg het laatste stukjetoe aan de lijst
    return codonLijst                   #return de lijst met codons

def tellen(codonLijst):                 #creeer de tellen functie, deze functie telt hoe vaak elk codon voorkomt in de sequentie
    gebLijst =[]                        #maak een lijst waar in komt te staan hoe vaak elk codon wordt gebruikt
    for i in range(64):                 #zo lang i in de range van 0 en 64 zit...
        gebLijst.append(0)              #voeg een 0 toe aan de gebLijst
    codLijst = ['ATT', 'ATC', 'ATA', 'CTT', 'CTC','CTA','CTG','TTA','TTG','GTT','GTC','GTA','GTG','TTT','TTC','ATG','TGT','TGC','GCT','GCC','GCA','GCG','GGT','GGC','GGA','GGG','CCT','CCC','CCA','CCG','ACT','ACC','ACA','ACG','TCT','TCC','TCA','TCG','AGT','AGC','TAT','TAC','TGG','CAA','CAG','AAT','AAC','CAT','CAC','GAA','GAG','GAT','GAC','AAA','AAG','CGT','CGC','CGA','CGG','AGA','AGG','TAA','TAG','TGA']
    for i in codonLijst:                #loop door de codonLijst...
        pos = codLijst.index(i)         #geef pos de waarde van de positie waar het codon zich bevindt in codLijst
        gebLijst[pos]+=1                #verhoog deze positie met 1
    return gebLijst                     #return delijst met hoe vaak een codon voorkomt
    
def dataSet(gebLijst):
    x = gebLijst                                                                                                                                                #kopieer gebLijstin x voor minder chaotisch programma
    totalenLijst = [x[0]+x[1]+x[2],    x[3]+x[4]+x[5]+x[6]+x[7]+x[8],    x[9]+x[10]+x[11]+x[12],   x[13]+x[14],    x[15],
                    x[16]+x[17],        x[18]+x[19]+x[20]+x[21],            x[22]+x[23]+x[24]+x[25],   x[26]+x[27]+x[28]+x[29],
                    x[30]+x[31]+x[32]+x[33],    x[34]+x[35]+x[36]+x[37]+x[38]+x[39],    x[40]+x[41],    x[42],    x[43]+x[44],
                    x[45]+x[46],    x[47]+x[48],    x[49]+x[50],    x[51]+x[52],    x[53]+x[54], x[55]+x[56]+x[57]+x[58]+x[59]+x[60],    x[61]+x[62]+x[63]]     #lijst met de aantallen codons die voor een aminozuur coderen

    tel = 0
    for i in totalenLijst:          #zorg dat er geen 0 staat i de totalenlijst om delen door 0 te voorkomen
        if i == 0:
            totalenLijst[tel] = 1
        tel+=1                      

    y = totalenLijst                #kopieer totalenLijst in y voor minder chaotisch programma

    perLijst = [x[0]/y[0], x[1]/y[0], x[2]/y[0], x[3]/y[1], x[4]/y[1], x[5]/y[1], x[6]/y[1], x[7]/y[1], x[8]/y[1], x[9]/y[2], x[10]/y[2],  
                x[11]/y[2], x[12]/y[2], x[13]/y[3], x[14]/y[3], x[15]/y[4], x[16]/y[5], x[17]/y[5], x[18]/y[6], x[19]/y[6], x[20]/y[6], x[21]/y[6], 
                x[22]/y[7], x[23]/y[7], x[24]/y[7], x[25]/y[7], x[26]/y[8], x[27]/y[8], x[28]/y[8], x[29]/y[8], x[30]/y[9], x[31]/y[9], x[32]/y[9], 
                x[33]/y[9], x[34]/y[10], x[35]/y[10], x[36]/y[10], x[37]/y[10], x[38]/y[10], x[39]/y[10], x[40]/y[11], x[41]/y[11], x[42]/y[12],
                x[43]/y[13], x[44]/y[13], x[45]/y[14], x[46]/y[14], x[47]/y[15], x[48]/y[15], x[49]/y[16], x[50]/y[16], x[51]/y[17], x[52]/y[17],
                x[53]/y[18], x[54]/y[18], x[55]/y[19], x[56]/y[19], x[57]/y[19], x[58]/y[19], x[59]/y[19], x[60]/y[19], x[61]/y[20], x[62]/y[20], x[63]/y[20]] #lijst met het codongebruik tov het totaal van het aminozuur
    
    tel = 0
    a = perLijst            #zorgt dat de lijst met percentages *100 wordt gedaan om juiste percentages tee verkrijgen
    for i in perLijst:
        a[tel] = a[tel]*100     
        tel+=1                     
        
    dataLijst = [[a[0],a[3],a[9] ,a[13],a[15],a[16],a[18],a[22],a[26],a[30],a[34],a[40],a[42],a[43],a[45],a[47],a[49],a[51],a[53],a[55],a[61]]
                ,[a[1],a[4],a[10],a[14],0    ,a[17],a[19],a[23],a[27],a[31],a[35],a[41],0    ,a[44],a[46],a[48],a[50],a[52],a[54],a[56],a[62]]
                ,[a[2],a[5],a[11],0    ,0    ,0    ,a[20],a[24],a[28],a[32],a[36],0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,a[57],a[63]]
                ,[0   ,a[6],a[12],0    ,0    ,0    ,a[21],a[25],a[29],a[33],a[37],0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,a[58],0]
                ,[0   ,a[7],0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,a[38],0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,a[59],0]
                ,[0   ,a[8],0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,a[39],0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,a[60],0]]     #lijst met percentages van codongebruik
    return dataLijst                                                                                                                            #return de dataLijst met percentages

#--------------------------------------------
#I L V F M C A G P T S Y W Q N H E D K R Stop
#3 6 4 2 1 2 4 4 4 4 6 2 1 2 2 2 2 2 2 6 3
#--------------------------------------------

def plotten(dataLijst):                                                                                                                                                 #creeer de plotten functie, met deze fucntie wordt de data weergeven
    codTekst = ['ATT', 'CTT', 'GTT', 'TTT', 'ATG', 'TGT', 'GCT', 'GGT', 'CCT', 'ACT', 'TCT', 'TAT', 'TGG', 'CAA', 'AAT', 'CAT', 'GAA', 'GAT', 'AAA', 'CGT', 'TAA',
                'ATC', 'CTC', 'GTC', 'TTC', '   ', 'TGC', 'GCC', 'GGC', 'CCC', 'ACC', 'TCC', 'TAC', '   ', 'CAG', 'AAC', 'CAC', 'GAG', 'GAC', 'AAG', 'CGC', 'TAG',
                'ATA', 'CTA', 'GTA', '   ', '   ', '   ', 'GCA', 'GGA', 'CCA', 'ACA', 'TCA', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'CGA', 'TGA',
                '   ', 'CTG', 'GTG', '   ', '   ', '   ', 'GCG', 'GGG', 'CCG', 'ACG', 'TCG', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'CGG', '   ',
                '   ', 'TTA', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'AGT', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'AGA', '   ',
                '   ', 'TTG', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'AGC', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'AGG', '   ']      #lijst met codons voor tekstweergavee in plot
    amLijst = ['I','L','V','F','M','C','A','G','P','T','S','Y','W','Q','N','H','E','D','K','R','Stop',]
    lijstLen = range(len(amLijst))                          #geef lijstLen de range zo lang als het aantal waarden in amLijst
    X = np.arange(len(dataLijst[0]))                        #geef X een lijstje met oplopende nummers ter grootte van de lengte van de sublijst in datalijst op positie 0
                
    plt.bar(X + 0.00, dataLijst[0], color = '#ffd699', width = 0.15, align = 'center')                              
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i]+0.00-0.05, dataLijst[0][i]+1.75, s = codTekst[i+00], rotation = 90, fontsize = 7)
    plt.bar(X + 0.15, dataLijst[1], color = '#b8ff99', width = 0.15, align = 'center')
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i]+0.15-0.05, dataLijst[1][i]+1.75, s = codTekst[i+21], rotation = 90, fontsize = 7)
    plt.bar(X + 0.30, dataLijst[2], color = '#99ffe7', width = 0.15, align = 'center')
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i]+0.30-0.05, dataLijst[2][i]+1.75, s = codTekst[i+42], rotation = 90, fontsize = 7)
    plt.bar(X + 0.45, dataLijst[3], color = '#99a5ff', width = 0.15, align = 'center')
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i]+0.45-0.05, dataLijst[3][i]+1.75, s = codTekst[i+63], rotation = 90, fontsize = 7)
    plt.bar(X + 0.60, dataLijst[4], color = '#dd99ff', width = 0.15, align = 'center')
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i]+0.60-0.05, dataLijst[4][i]+1.75, s = codTekst[i+84], rotation = 90, fontsize = 7)
    plt.bar(X + 0.75, dataLijst[5], color = '#ff99c0', width = 0.15, align = 'center')
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i]+0.75-0.05, dataLijst[5][i]+1.75, s = codTekst[i+105], rotation = 90, fontsize = 7)

    plt.ylim(0,105)                                         #maak de hoogte van de y as 105
    plt.xticks(lijstLen, amLijst)                           #zet de letters van aminozuren op de x as
    plt.title('codongebruik in procenten per aminozuur')
    plt.xlabel('aminozuur')
    plt.ylabel('percentage codongebruik')
    plt.show()

main()








































'''
def kaPlottenFunctie(dataLijst, codLijst):                                                                                 deze functie werkt niet lmaoooooooooo
    amLijst = ['I','L','V','F','M','C','A','G','P','T','S','Y','W','Q','N','H','E','D','K','R','Stop',]

    print(amLijst)
    print(dataLijst[0])
    print(dataLijst[1])
    print(dataLijst[2])
    print(dataLijst[3])
    print(dataLijst[4])
    print(dataLijst[5],'\n')
    kleur = ['#ff5252', 'lightblue', '#d77fc1', 'lavender', 'pink', 'lightgreen']

    lijstLen = range(len(amLijst))
    bottomLijst = []
    num=0
    for i in dataLijst[0]:
        comb = dataLijst[0][num]+dataLijst[1][num]
        bottomLijst.append(comb)
        num+=1
    print(bottomLijst)

    plt.bar(lijstLen, dataLijst[0], color='#ff5252')
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i], dataLijst[0][i], s = dataLijst[0][i])
        
    plt.bar(lijstLen, dataLijst[1], color='lightblue', bottom = dataLijst[0])
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i], bottomLijst[i], s = dataLijst[1][i])

    plt.bar(lijstLen, dataLijst[2], color='#d77fc1', bottom = bottomLijst)
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i], bottomLijst[i], s = dataLijst[2][i])
     
    num=0
    for index in dataLijst[0]:
        bottomLijst[num] = bottomLijst[num] + dataLijst[2][num]
        num+=1
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i], bottomLijst[i], s = dataLijst[3][i])
    plt.bar(lijstLen, dataLijst[3], color='lavender', bottom = bottomLijst)

    num=0
    for index in dataLijst[0]:
        bottomLijst[num] = bottomLijst[num] + dataLijst[3][num]
        num+=1
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i], bottomLijst[i], s = dataLijst[4][i])
    plt.bar(lijstLen, dataLijst[4], color='pink', bottom = bottomLijst)

    num=0
    for index in dataLijst[0]:
        bottomLijst[num] = bottomLijst[num] + dataLijst[4][num]
        num+=1        
    for i in range(len(lijstLen)):
        plt.text(lijstLen[i], bottomLijst[i], s = dataLijst[5][i])
    plt.bar(lijstLen, dataLijst[5], color='lightgreen', bottom = bottomLijst)
    plt.text(lijstLen[i], bottomLijst[i], s = dataLijst[5][i])
 
        
    
    dec = (max(bottomLijst))
    plt.ylim([0,dec+20])
    plt.xticks(lijstLen, amLijst)
    plt.show()
'''
