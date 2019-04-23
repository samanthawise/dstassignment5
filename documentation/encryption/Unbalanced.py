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
    return(Markov.babble(100000))
def Generator_small(Markov):
    return(Markov.babble(1000))

# time calculate
import matplotlib.pyplot as plt
import random
random.seed(4*7)
import time
import functools
timesaver = []
# Set a probability p
p = 1

start_time = time.time()
data = Generator(m)
data = bytes(data, encoding = "utf-8")
data_small = Generator_small(m)
data_small = bytes(data_small, encoding = "utf-8")
print("generating time:",time.time()-start_time)
for j in range(0,5000,1000):
    dataset = []
    #start_time = time.time()
    for i in range(j):
        if random.uniform(0, 1)<p:
            dataset.append(data_small)
        else:
            dataset.append(data)
    #dataset = bytes(dataset, encoding = "utf-8")
    #dataset = list(map(functools.partial(bytes, encoding="utf-8"), dataset))
    start_time = time.time()
    test = list(map(Encrypt,dataset))
    decoded = list(map(Decrypt,test))

    end_time = time.time() - start_time
    print(end_time)
    timesaver.append(end_time)
import pickle
with open('../data/time_unbalanced_100.pickle', 'wb') as f:
    pickle.dump(timesaver, f)

