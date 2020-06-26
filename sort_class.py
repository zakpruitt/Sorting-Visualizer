import random
import time
import os
import stopwatch

class Sorter:
    def __init__(self):
      """ Initializes Sorter object with just an array for a data member. """  
      self.array = []

    def PopulateArray(self, minValue, maxValue, populationSize):
        """ Populates array with random, distinct integers. """
        
        # resets array
        self.array = []
        
        for _ in range(populationSize): # _ = unused
            number = random.randint(minValue, maxValue+1)
            
            if number in self.array:
                # number generated is not distinct
                while number in self.array:
                    number = random.randint(minValue, maxValue+1)
                self.array.append(number)
            else:
                # number generated is distinct
                self.array.append(number)
        
    def BubbleSort(self, delay, draw_data):
        """ Sorts an array via swapping elements if the next is greater. """
        timer = stopwatch.Timer()
        timer.start()
        passNumber = 0

        for i in range(len(self.array)):
            passNumber += 1
            for j in range(0, len(self.array) - i - 1): # last i elements are already in place 
                if self.array[j] > self.array[j+1] :  # Swap if the element found is greater    
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    draw_data(self.array, ['green' if x == j or x == j+1 else 'red' for x in range(len(self.array))] )
                    time.sleep(delay)
        
        print(timer.stop())
            
