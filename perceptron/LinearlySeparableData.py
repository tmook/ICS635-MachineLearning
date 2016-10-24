#!/usr/bin/env python
import numpy as np
from random import uniform

class LinearlySeparableData:
   def __init__(self, totalLabels=None, fileName=None):
      #init all member variables
      self.trueSlope = 0.0
      self.trueIntercept = 0.0
      self.upperIntercept = 0.0
      self.lowerIntercept = 0.0
      self.DataPointsPerLabel = [[],[]]
      if totalLabels != None:
         self.DataPointsPerLabel = [[] for i in range(0, totalLabels)]
      if fileName != None:
         importDataSet(fileName)
         

   ## This will generate data points above and below a line. Calling this 
   ## function multiple times will add new data points to the dataset. 
   ## e.g. if you call this function 5 times, 5 new sets will be added
   ## Line with is how far away from the line the data starts to generate
   ## ratio is from 0 to 1 of how many point above the line (default: 0.5)
   ## e.g 1 is 100% ponts above line, 0.5 is 50% point above line, 0 is 0% points above line
   def generateData(self, slope=0.0, intercept=0.0, data_size=10, lineWidth=0.0, ratio=0.5):
      #initialize lines paramenters
      self.trueSlope = slope
      self.upperIntercept = self.lowerIntercept = self.trueIntercept = intercept

      #generate line width
      if lineWidth > 0:
         #generate upper line
         self.upperIntercept += lineWidth/2
         #generate lower line
         self.lowerIntercept -= lineWidth/2

      #generate data
      while(self.getTotalDataPoints() < data_size):
         point = [uniform(-10,10),uniform(-10,10)]
         result = self.trueSlope*point[0] + self.trueIntercept - point[1]
         #generate data below line
         if (result>0) and (len(self.DataPointsPerLabel[0]) < (1-ratio)*data_size):
            if (self.trueSlope*point[0] + self.lowerIntercept - point[1]) > 0:
               self.DataPointsPerLabel[0].append([list(point),-1])
         #generate data above line
         if (result<0) and (len(self.DataPointsPerLabel[1]) < ratio*data_size):
            if (self.trueSlope*point[0] + self.upperIntercept - point[1]) < 0:
               self.DataPointsPerLabel[1].append([list(point),1])


   def logicANDdata(self):
      return list([ [[0,0],-1], [[0,1],-1], [[1,0],-1], [[1,1],1] ])

   
   def logicORdata(self):
      return list([ [[0,0],-1], [[0,1],1], [[1,0],1], [[1,1],1] ])


   def logicXORdata(self):
      return list([ [[0,0],-1], [[0,1],1], [[1,0],1], [[1,1],-1] ])


   def getDataSet(self):
      dataset = []
      for labelSet in self.DataPointsPerLabel:
         for point in labelSet:
            dataset.append(point)
      return list(dataset)


   def getTrueSlope(self):
      return list(self.trueSlope)


   def getTrueIntercept(self):
      return self.trueIntercept


   def getUpperIntercept(self):
      return list(self.upperIntercept)


   def getLowerIntercept(self):
      return list(self.lowerIntercept)


   def getTotalDataPoints(self):
      total = 0
      for labelSet in self.DataPointsPerLabel:
         total += len(labelSet)
      return total

   def printInfo(self):
      for idx, labelSet in enumerate(self.DataPointsPerLabel):
         print "Label: "+str(idx)
         print "Total Points: "+str(len(labelSet))
         print "Data Points: "
         print labelSet
         print ""


   ## this function clears the dataset
   def clearAll(self):
      self.trueSlope = 0.0
      self.trueIntercept = 0.0
      self.upperIntercept = 0.0
      self.lowerIntercept = 0.0
      self.DataPointsPerLabel = [[],[]]
   
   ## returns true lines
   def getPlotTuple(self):
      return self.trueSlope, self.trueIntercept, self.upperIntercept, self.lowerIntercept


   def plot(self):
      import matplotlib.pyplot as plt
      lbl = ['ro','bx']
      #plot points in dataset
      for idx, labelSet in enumerate(self.DataPointsPerLabel):
         for point in labelSet:
            plt.plot(point[0][0], point[0][1], lbl[idx])
      #plot true line
      Y = range(-10,11)
      X = []
      if self.trueSlope == 0:
         X = range(-10,11)
         Y = [self.trueIntercept]*len(X)
      else:
         for y in Y:
            X.append((y- self.trueIntercept)/self.trueSlope)
      plt.plot(X,Y)
      #plot upper line
      Y = range(-10,11)
      X = []
      if self.trueSlope == 0:
         X = range(-10,11)
         Y = [self.upperIntercept]*len(X)
      else:
         for y in Y:
            X.append((y- self.upperIntercept)/self.trueSlope)
      plt.plot(X,Y, color='c')
      #plot lower line
      Y = range(-10,11)
      X = []
      if self.trueSlope == 0:
         X = range(-10,11)
         Y = [self.lowerIntercept]*len(X)
      else:
         for y in Y:
            X.append((y- self.lowerIntercept)/self.trueSlope)
      plt.plot(X,Y,color='m')
      plt.show()
         

   def ImportData(self, filename=None):
      if filename == None:
         print "provide file name for importData"
      else:
         pass


   def ExportData(self, filename=None):
      if filename == None:
         print "provide file name for ExportData"
      else:
         pass



###### Run this test of this script is main
if __name__ == "__main__":
   lsd = LinearlySeparableData()
   lsd.generateData()
   lsd.printInfo()
   #lsd.plot()

   lsd = LinearlySeparableData()
   lsd.generateData(slope=-2.0)
   #lsd.plot()

   lsd = LinearlySeparableData()
   lsd.generateData(slope=-2.0,intercept=3.0)
   #lsd.plot()

   #def generateData(self, slope=0.0, intercept=0.0, data_size=10, lineWidth=0.0, ratio=0.5):
   lsd = LinearlySeparableData()
   lsd.generateData(slope=-2.0,intercept=-3.0,lineWidth=10.0)
   #lsd.plot()

   lsd = LinearlySeparableData()
   lsd.generateData(slope=-2.0,intercept=-3.0,lineWidth=10.0, ratio=0.4)
   #lsd.plot()

   lsd = LinearlySeparableData()
   lsd.generateData(slope=-2.0,intercept=-3.0, data_size=100,lineWidth=10.0, ratio=0.4)
   lsd.plot()
