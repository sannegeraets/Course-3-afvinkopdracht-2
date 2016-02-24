"""
Het beste kan een staafdiagram gebruikt worden voor het weergeven
van de frequentie waarmee een codon in de sequentie zit.

Maak een grafiek met matplotlib die een weergave van het
humane p53 gen.

Zorg dat de grafiek ook laat zien dat voor hetzelfde aminozuur
verschillende codons gebruikt kan worden
"""

import matplotlib.pyplot as plt

def main():  
    try:
        bestand = openbestand()
        seqq = sequentie(bestand)
        seq = sfilter(seqq)
        print(seq)
        codons = create_codons(seq)
        print(" ".join(codons))
        codon_lijst, number_lijst = lijsten(codons)
        plot_bars(codon_lijst, number_lijst)
    except IOError:
        print("Er is iets fout gegaan bij het openen van het bestand, probeer het opnieuw.")
    except:
        print("Er is iets fout gedaan.")



def openbestand():
    file = open("m_p53.gb", "r")
    bestand = file.read().upper()
    return bestand
    

def sequentie(bestand):
    seq = bestand.split("ORIGIN")
    return seq[1]


def sfilter(seqq):
    seq1 = []
    for i in seqq:
        if i == "A" or i == "C" or i == "G" or i == "T":
            seq1.append(i)
    seq = "".join(seq1)
    return seq


def create_codons(seq):
    start = seq.index("ATG")
    done = 0
    codons = []
    if start != -1:
        while start + 2 < len(seq) and done != 1:
            codon = seq[start:start + 3]
            if codon == "TAG" or codon == "TAA" or codon == "TGA":
                done = 1
            if not codon == "TAG" or codon == "TAA" or codon == "TGA":
                codons.append(codon)
                start += 3
    return codons

    
def lijsten(codons):
#    dict_codon = {}
#    for codon in codons:
#        codon_count = codons.count(codon)
#        if codon not in dict_codon:
#            dict_codon[codon] = codon_count
    codon_lijst = []
    number_lijst = []
    for codon in codons:
        if codon not in codon_lijst:
            codon_lijst.append(codon)
            number_lijst.append(codons.count(codon))
    return codon_lijst, number_lijst
    
    
def plot_bars(codon_lijst, number_lijst):
    lijst = []
    totaal = 0
    for x in codon_lijst:
        totaal += 1
    for x in range(1, totaal + 1):
        lijst.append(x)
        
        
    plt.bar(lijst, number_lijst, label = "codons", color = "r")
    plt.xticks(lijst, codon_lijst, rotation = 90)
    plt.xlabel("codon")
    plt.ylabel("aantal")
    plt.title("frequentie codons in sequentie")
    plt.legend()
    plt.show()


main()
