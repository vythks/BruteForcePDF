import fitz
import os
from tqdm import tqdm 

class BruteForce:
    def __init__(self):
        print('Crack PDF')
    def Bruteforce(self):
        mypdf = input('[PDF] - ')
        self.load = []
        def Check(pdf):
            epdf = fitz.Document(pdf)
            return epdf.isEncrypted
        Check(mypdf)
        def Decode(file):
            if Check(file):
                pdf = fitz.open(file) 
                with open('PayLoad.txt','r') as payload:
                    for load in tqdm(payload):
                        try:
                            if pdf.authenticate(load[:-1]):
                                pdf.save('CrackedPDF.pdf')
                                self.load.append(load[:-1])
                                break
                            else:
                                pass
                        except:
                            pass
                with open('PdfKey.txt','w') as payload:
                        for load in tqdm(self.load):
                            payload.write(load+'\n')
        Decode(mypdf)
        
bruteforce = BruteForce()
bruteforce.Bruteforce()
