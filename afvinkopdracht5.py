import re

class DNA:


    def __init__(self, dna):
        self.setDNA(dna)
        
        
    def setDNA(self,dna):
        try:
            self.DNA = dna
            checkdna = re.match('^[ATGCN]*$', self.DNA.upper())
            if checkdna == None:
                raise SystemError
        except SystemError:
            print("Dit is geen DNA sequentie")

    def getDNA(self):        
        return self.DNA

    def getGC(self):
        g = self.DNA.count("G")
        c = self.DNA.count("C")
        GC = (g+c)/len(self.DNA)*100
        return GC

    def getTranscript(self):
        RNA = self.DNA.replace("A", "U").replace("T", "A").replace("G", "C").replace("C", "G")
        return RNA
        

    def getLength(self):
        return len(self.DNA), "nucleotides"

def openFile():
    try:
        bestand = open("Felis_catus.Felis_catus_8.0.cdna.all.fa", "r")
    except Exception as e:
        print("Error")
        raise SystemExit
    
    headers = []
    seqs = []
    seq=""
    for line in bestand:
        line = line.strip()
        if not line.startswith(">"):
            seq += line
        if line.startswith(">") and seq is not '':
            seqs.append(DNA(seq))
            seq = ""
    return seqs
            
def GCpercentage(seqs):
    gclijst = []
    for sequence in seqs:
        gclijst.append(sequence.getGC())

    i = (gclijst.index(max(gclijst)))
    print(seqs[i].getGC(), "%")
    print(seqs[i].getTranscript())
    print(seqs[i].getLength())

def main():
    seqs = openFile()
    GCpercentage(seqs)
    #print(seqs[:3])






main()
