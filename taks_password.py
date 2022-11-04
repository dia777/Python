import random

mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minus = "abcdefghijklmnñopqrstuvwxyz"
num = "0123456789"

all=mayus+minus+num

cant = 9

for i in range (8 and 16):
    password="".join(random.sample(all,cant))
    print (password)