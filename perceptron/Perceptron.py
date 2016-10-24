#!/usr/bin/env python

# perceptron algorithm
# input dataset is of feaures(is a list) and labels 
#    (e.g. [ [[0,0], -1], [[0,1], 1], [[1,0], 1], [[1,1], 1] ] )
# default value of maxIter=300
# FIXME: return weights? output is a linear decision boundary. (2D-Line, 3D-Plane, 4D-Cube, etc.)
from copy import deepcopy


class Perceptron:
   def __init__(self, maxIter=300):
      #init all memeber variables
      self.maxIterations = maxIter
      self.InitialIterations = maxIter
      self.labels = []
      self.errorHistory = []
      self.weights = []
      self.bias = 1
      self.learnRate = 0.5
      self.slope = 0
      self.intercept = 0

   def resetVariables(self):
      self.labels = []
      self.errorHistory = []
      self.weights = []


   def getLabels(self):
      return self.labels


   def getErrors(self):
      return self.errorHistory


   def getWeights(self):
      return self.weights


   def getIterations(self):
      return self.InitialIterations - self.maxIterations


   def setBias(self, b):
      self.Bias = b


   def setLearnRate(self, c):
      self.learnRate = c


   def step_function(self, x):
      return -1 if x < 0 else 1


   def dotProduct(self, vectorA, vectorB):
      #dot product of two vecotrs is the sum of the product each
      #parallel component (like a weighted sum)
      product = 0
      for i in range( 0,len(vectorA) ):
         product += vectorA[i]*vectorB[i]
      return product


   def addBiasComponent(self, dataSet):
      #add bias to dataSet
      for point in dataSet:
         point[0].insert(0, self.bias)


   # Perceptron algorithm
   # loop while there are still missclassified points or max iterations is reached
   # calculate label output
   #   get dot product of weight and current data point
   #   apply result of dot product through step function
   #   append step function result to label list
   # update weights
   #   learningRate * (expected - result) * dataPoint
   def fit(self, data=[], w=None, b=None, c=None, plotIon=-1):
      self.resetVariables()
      #add bias to dataset
      dataSet = deepcopy(data)
      self.addBiasComponent( dataSet )
      #set weights
      if w:
         self.weights = list(w)
      else:
         self.weights = [1.0]*(len(dataSet[0][0]))
      #set bias
      if b:
         self.setBias(b)
      #set learning rate
      if c:
         self.setLearnRate(c)
      #set label list size
      self.labels = [1]*len(dataSet)
      #reset max iterations
      self.maxIterations = self.InitialIterations

      errorCount = 1
      while (errorCount > 0) and (self.maxIterations > 0):
         self.maxIterations -= 1
         errorCount = 0

         #calculate label of data point (perceptron algorithm)
         for i,point in enumerate(dataSet):
            expectedLabel = point[1]
            product = self.dotProduct(self.weights, point[0])
            results = self.step_function(product)
            
            #update label list with results
            self.labels[i] = results

            if expectedLabel != results:
               #update error count
               errorCount += 1
               #update weights
               for idx, feature in enumerate(point[0]):
                  self.weights[idx] += self.learnRate * (expectedLabel - results) * feature

         #save slope and itercept
         if self.weights[2] != 0:
            self.slope = -(self.weights[1]/self.weights[2])
            self.intercept = -(self.weights[0]/self.weights[2])
         else:
            self.slope = self.intercept = 0.0
         #keep track errors per iteration
         self.errorHistory.append(errorCount)
         #plot each iteration
         if plotIon > -1:
            self.plot(data, ion=plotIon)

      return self.slope, self.intercept
      #return "y = "+ str(self.slope)+"x + ("+str(self.intercept)+")"

   def plot(self, data, trueLineTuple=None, ion=-1):
      import matplotlib.pyplot as plt
      plt.axis([-10,10,-10,10])
      #plot points in dataset
      for point in data:
         if(point[1] < 1):
            plt.plot(point[0][0], point[0][1], 'ro')
         else:
            plt.plot(point[0][0], point[0][1], 'bx')

      #plot perceptron line
      Y = range(-10,11)
      X = []
      if self.slope == 0:
         X = range(-10,11)
         Y = [self.intercept]*len(X)
      else:
         for y in Y:
            X.append((y- self.intercept)/self.slope)
      plt.plot(X,Y,'r')

      #if have true lines, plot them
      if trueLineTuple:
         trueSlope = trueLineTuple[0]
         trueIntercept = trueLineTuple[1]
         upperIntercept = trueLineTuple[2]
         lowerIntercept = trueLineTuple[3]
         #plot true line
         Y = range(-10,11)
         X = []
         if trueSlope == 0:
            X = range(-10,11)
            Y = [trueIntercept]*len(X)
         else:
            for y in Y:
               X.append((y- trueIntercept)/trueSlope)
         plt.plot(X,Y)
         #plot upper line
         Y = range(-10,11)
         X = []
         if trueSlope == 0:
            X = range(-10,11)
            Y = [upperIntercept]*len(X)
         else:
            for y in Y:
               X.append((y- upperIntercept)/trueSlope)
         plt.plot(X,Y,'c--')
         #plot lower line
         Y = range(-10,11)
         X = []
         if trueSlope == 0:
            X = range(-10,11)
            Y = [lowerIntercept]*len(X)
         else:
            for y in Y:
               X.append((y- lowerIntercept)/trueSlope)
         plt.plot(X,Y,'c--')
      #show plot
      if (ion > -1):
         plt.ion()
         plt.pause(ion)
      else:
         plt.show()
      #clear figure
      plt.clf()


###### Run this test of this script is main
if __name__ == "__main__":
   #tests
   andData = [ [[0,0],-1], [[0,1],-1], [[1,0],-1], [[1,1],1] ] 
   orData = [ [[0,0],-1], [[0,1],1], [[1,0],1], [[1,1],1] ] 
   xorData = [ [[0,0],-1], [[0,1],1], [[1,0],1], [[1,1],-1] ] 
  
   # AND data
   pn = Perceptron()
   print pn.fit(andData)
   print pn.getLabels(), pn.getIterations()
   print pn.getWeights()
   print pn.getErrors()
   print pn.fit(andData)
   print pn.getLabels(), pn.getIterations()
   print pn.getWeights()
   print pn.getErrors()
   print pn.fit(andData)
   print pn.getLabels(), pn.getIterations()
   print pn.getWeights()
   print pn.getErrors()

   # OR Data
   print ""
   pn = Perceptron()
   print pn.fit(orData)
   print pn.getLabels(), pn.getIterations()
   print pn.getWeights()
   print pn.getErrors()

   # XOR Data
   print ""
   print "xor"
   pn = Perceptron()
   print pn.fit(xorData,c=1)
   print pn.getLabels(), pn.getIterations()
   print pn.getWeights()
   print pn.getErrors()

   #pn = Perceptron()
   #s,i = pn.fit(andData,plotIon=3)
   #pn.plot(andData)
