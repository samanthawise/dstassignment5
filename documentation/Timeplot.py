from MC import MarkovChain
from bitarray import bitarray
from cryptography.fernet import Fernet


import sys
sys.setrecursionlimit(150000)

with open ("../books/3001.txt", "r", encoding="utf-8") as myfile:
    data = myfile.readlines()

m = MarkovChain()

for i in data:
    m.learn(i)

length = 10000
m.babble(length)
def Encrypt(data):
    key = Fernet.generate_key()
    f = Fernet(key)
    ciphertext = f.encrypt(data)
    return(key, ciphertext)

def Decrypt(key_ciphertext):
    f = Fernet(key_ciphertext[0])
    decrypttext = f.decrypt(key_ciphertext[1])
    return(decrypttext)

def Generator(Markov):
    return(Markov.babble(10000))

# time calculate
import matplotlib.pyplot as plt

import time
import functools
timesaver = []

for j in range(1000,501000,10000):
    start_time = time.time()
    dataset = []
    data = Generator(m)
    data = bytes(data, encoding = "utf-8")
    for i in range(j):
        dataset.append(data)
    #dataset = bytes(dataset, encoding = "utf-8")
    #dataset = list(map(functools.partial(bytes, encoding="utf-8"), dataset))
    test = list(map(Encrypt,dataset))
    decoded = list(map(Decrypt,test))

    end_time = time.time() - start_time
    print(end_time)
    timesaver.append(end_time)
import pickle
with open('../data/time.pickle', 'wb') as f:
    pickle.dump(timesaver, f)
