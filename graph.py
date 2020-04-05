import math
import random


def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        
        self.f=open(filename,'r')
        sourceInLine=self.f.readlines()
        lenOfLine = len(sourceInLine)

        if n == -1:
            # self.dist[i][j]
            self.n = len(sourceInLine)
            finalList = []
            self.dists = [[0 for i in range(self.n)] for j in range(self.n)]
            
            for i in range(lenOfLine):
                line = sourceInLine[i] 
                line.strip('\n')
                line.lstrip()
                dataset = [int(j) for j in line.split()]
                finalList.append(dataset)


            for i in range(lenOfLine):
                for j in range(lenOfLine):
                    self.dists[i][j] = euclid(finalList[i],finalList[j])    

            self.perm = [i for i in range(self.n)]

        else:

            self.n = n
            self.dists = [[0 for i in range(self.n)] for j in range(self.n)]
            
            for i in range(lenOfLine):
                line = sourceInLine[i]
                line.strip('\n')
                line.lstrip()
                dataset = [int(j) for j in line.split()]
                
                x = dataset[0]
                y = dataset[1]
                cost = dataset[2]

                self.dists[x][y] = cost
                self.dists[y][x] = cost
                
            
            self.perm = [i for i in range(self.n)]


    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        result = 0
        for i in range(self.n-1):
            start = self.perm[i]
            end = self.perm[i +1]
            result = result + self.dists[start][end]
        result = result + self.dists[self.perm[-1]][self.perm[0]]
        return result


    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
   
    def trySwap(self,i):

        # tourValueOforiginal
        OriginalPerm = [int(i) for i in self.perm]
        OriginTourValue = self.tourValue()
        
        # tourValueOfswap
        temp1 = OriginalPerm[i]
        temp2 = OriginalPerm[(i+1) % self.n]
        self.perm[i] = temp2
        self.perm[(i+1) % self.n] = temp1
        SwapTourValue = self.tourValue()


        if (OriginTourValue > SwapTourValue):
            return True
        else:
            self.perm = OriginalPerm
            return False
    

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):

        # tourValueOforiginal
        OriginalPerm = [int(i) for i in self.perm]
        OriginTourValue = self.tourValue()
        
        # tourValueOfswap
        reversePerm = OriginalPerm[i:j + 1]
        reversePerm.reverse()
        reversePerm = OriginalPerm[:i] + reversePerm + OriginalPerm[j+1:]
        self.perm = reversePerm
        SwapTourValue = self.tourValue()
        

        if (OriginTourValue > (SwapTourValue)):
            return True
        else:
            self.perm = OriginalPerm
            return False
                

    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True



    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
                

    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
       
        #Original
        OriginalPerm = [int(i) for i in self.perm]
        lenPerm = len(OriginalPerm)
        NewPerm = [OriginalPerm[0]]
        nextNode = 0
        OriginalPerm.pop(0)

        while (len(OriginalPerm) > 0):
            miniValue = math.inf

            for j in range(lenPerm):
                 
                 if (j not in NewPerm):
                    if (self.dists[nextNode][j] <  miniValue):
                        miniValue = self.dists[nextNode][j] 
                        index = j
            if index not in NewPerm:
                nextNode = index
                NewPerm.append(nextNode)
                OriginalPerm.remove(nextNode)

        self.perm = NewPerm



    def UniversalGreedy(self):

        # Overall Greedy
        OriginalPerm = [int(i) for i in self.perm]
        lenPerm = len(OriginalPerm)
        miniValue = math.inf

        # find the starting node which is the lowest cost of tourValue
        for i in range(lenPerm):
            for j in range(lenPerm):
                if (i != j):
                    if (self.dists[i][j] <  miniValue):
                        miniValue = self.dists[i][j] 
                        startIndex = i
                        endIndex = j

        NewPerm = [startIndex]
        NewPerm.append(endIndex)

        OriginalPerm.remove(startIndex)
        OriginalPerm.remove(endIndex)
        nextNode = endIndex
        
        # Greedy Algorithm 
        while (len(OriginalPerm) > 0):
            miniValue = math.inf

            for j in range(lenPerm):
                 
                 if (j not in NewPerm):
                    if (self.dists[nextNode][j] <  miniValue):
                        miniValue = self.dists[nextNode][j] 
                        index = j
            if index not in NewPerm:
                nextNode = index
                NewPerm.append(nextNode)
                OriginalPerm.remove(nextNode)

        self.perm = NewPerm

        # the reverse function to avoid the local minimum
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True




  









                            

            


