import os
import numpy as np

numGiocatori = 100
numTentativi = 10000

numwin=0
numwinprimogiocatore=0
numlossprimogiocatore=0

numloss=0
for j in range(numTentativi):
    numeridentroscatole = []
#init

    numeriscatole = np.random.choice(numGiocatori, numGiocatori, replace=False)
    numeridentroscatole = np.random.choice(numGiocatori, numGiocatori, replace=False)
    maxAttempts = 0

    for i in range(numGiocatori):
        attempts = 0
        found=False
        start = i
        while (found == False):
            attempts=attempts+1
            if numeridentroscatole[start] == i:
                found = True
            start =  numeridentroscatole[start]
        if attempts > maxAttempts:
            maxAttempts = attempts

#    print("   ---> MAX attempts", maxAttempts)
        if i ==0:
            if maxAttempts>=numGiocatori/2:
                numlossprimogiocatore = numlossprimogiocatore+1
            else:
                numwinprimogiocatore = numwinprimogiocatore+1
    if maxAttempts>=numGiocatori/2:
        numloss = numloss+1
    else:
        numwin = numwin+1

print ("FINAL STATS")
print ("FracWin: ", numwin/numTentativi)
print ("FracWinPrimoGiocatore: ", numwinprimogiocatore/numTentativi)    


    

