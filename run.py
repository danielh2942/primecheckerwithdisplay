from PIL import Image
from math import sqrt
from random import randint
#Check Prime
hexa = []
primes = [2]
colors = [(255,255,255)]
n = 1
prime = 0
img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        print n
        f = n
        while True:
            if f % primes[prime] == 0 and primes[prime] <= sqrt(f): #true if not a prime
                n = n + 1
                pixels[i,j] = colors[prime] #the lowest prime it divides into to avoid conflicts
                prime = 0
                break
            if primes[prime] > sqrt(f) and f != 1: #true if prime
                newcolor = (randint(0,255),randint(0,255),randint(0,255)) #unique color for this number and it's multiples
                primes.append(f)
                pixels[i,j] = newcolor
                colors.append(newcolor)
                prime = 0
                n = n + 1
                break
            if f == 1: #true if 1
                pixels[i,j] = (0,0,0)
                n = n + 1
                break
            else:
                prime = prime + 1

img.save("C:/Users/HP/Desktop/out.bmp")
