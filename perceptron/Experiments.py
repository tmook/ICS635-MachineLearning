#!/usr/bin/env python
from Perceptron import Perceptron
from LinearlySeparableData import LinearlySeparableData


###############################################
### Experiment 1                            ###
### plot of percptron with logic AND data   ###
###############################################
def Experiment1():
   lsd = LinearlySeparableData()

   data = lsd.logicANDdata()
   pn = Perceptron()
   pn.fit(data,plotIon=2)
   print pn.getIterations(), pn.getErrors()


###############################################
### Experiment 2                            ###
### plot of percptron with logic OR data    ###
###############################################
def Experiment2():
   lsd = LinearlySeparableData()

   data = lsd.logicORdata()
   pn = Perceptron()
   pn.fit(data,plotIon=2)
   print pn.getIterations(), pn.getErrors()


###############################################
### Experiment 3                            ###
### plot of percptron with logic XOR data   ###
###############################################
def Experiment3():
   lsd = LinearlySeparableData()

   data = lsd.logicXORdata()
   pn = Perceptron()
   pn.fit(data,c=1,plotIon=0.1)
   print pn.getIterations(), pn.getErrors()


###############################################
### Experiment 4                            ###
### percptron on ranomly generated data,plot###
###############################################
def Experiment4():
   lsd = LinearlySeparableData()
   lsd.generateData(slope=-2.0,intercept=-3.0,data_size=100)

   data = lsd.getDataSet()
   pn = Perceptron()
   pn.fit(data,plotIon=2)
   print pn.getIterations(), pn.getErrors()




### uncomment a test to run Experiements ###
#Experiment1()
#Experiment2()
#Experiment3()
Experiment4()









