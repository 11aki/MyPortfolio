import time
import datetime 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 

farBack = 500

def testdata():
    dateC = []
    priceC = []
    volC = []

    try:
        scode = open('btc.csv','r').read()
        splitSource = scode.split('/n')
        print(scode)

        for eachLine in splitSource[-farBack]:
            splitLine = eachLine.split(',')
            dateC = splitLine[0]
            priceC = splitLine[1]
            volC = splitLine[2]

            dateC = append(float(dateC))
            priceC = append(float(priceC))
            volC = append(float(volC))
    except :
        print("error")


    plt.plot(dateC,priceC)
    plt.show()



testdata()