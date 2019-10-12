from time import sleep
from random import uniform
import sys

f = open('Sample.txt', 'r')

for line in f:
    for c in line:
        print(c, end='', flush=True)
        sleep(uniform(0,0.15))
f.close()
