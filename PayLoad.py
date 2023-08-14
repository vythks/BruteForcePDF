import string
import random
import os
from tqdm import tqdm

class PayLoad:
    def __init__(self):
        print('Deploying Payload')    
    def Options(self):
        self.option = string.digits
        self.length = 6
    def Generator(self):
        self.Options()  
        def Endpoint(option=self.option,length=self.length):
            global number
            number = len(option)
            digits = number
            power = int(length)-1
            for powers in tqdm(range(power)):
                number*=digits
        Endpoint()
        def Generate():
            self.payload = set()
            while True:
                self.payload.add(''.join(map(str,random.choices(self.option,k=int(self.length)))))
                if len(self.payload) == number:
                        break
        Generate()    
        def Sort():
            self.sorted_payload = list(self.payload)
            self.sorted_payload.sort()
        Sort()  
    def Export(self):
        self.Generator()  
        with open("PayLoad.txt",'w') as payload:
            for load in tqdm(self.sorted_payload):
                payload.write(load+'\n')
payload = PayLoad()
payload.Export()
