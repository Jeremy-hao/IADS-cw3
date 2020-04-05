import math
import graph
import numpy.matlib
import numpy 
import random


Option = input("Option: Euclidean OR Metric: ")
if (Option == "Euclidean"):
        weight = input("weight:")
        number = input("number:")
        g = numpy.random.randint(1,int(weight),size = [int(number),2])
        n = len(g)

        fileName = "cities100-version5"
        f = open(fileName,"x")
        for i in range(n):
            list = [int(i) for i in g[i]]    
            print(list[0],list[1],file = f)
        f.close()

        g = graph.Graph(-1,fileName)
        print("Original TourValue:",g.tourValue())

        g = graph.Graph(-1,fileName)
        g.swapHeuristic()
        g.tourValue()
        print("Swap TourValue: ",g.tourValue())

        g = graph.Graph(-1,fileName)
        g.swapHeuristic()
        g.TwoOptHeuristic()
        print("Swap&TwoOpt TourValue: ",g.tourValue())

        g = graph.Graph(-1,fileName)
        g.Greedy()
        print("Greedy TourValue: ",g.tourValue())

        g = graph.Graph(-1,fileName)
        g.UniversalGreedy()
        print("my own algorithm: ",g.tourValue())




if (Option == "Metric"):
           
    weightMax = input("weight:")
    number = input("number:")
    weightMax = int(weightMax)
    number = int (number)
    
    Final_list = []
    for i in range(number,-1,-1):
        for j in range(i):
            if (i != j):
                weightRandom = random.randint(1,weightMax)
                list = [j]
                list.append(i)
                list.append(weightRandom)
                Final_list.append(list)

    Final_list.pop(0)
    unique_list = [number]
    unique_list.append(0)
    unique_list.append(random.randint(1,weightMax))
    Final_list.append(unique_list)
       
    #print(Final_list)          
        
    fileName = "Metric100-plus"
    f = open(fileName,"x")
    for i in range(len(Final_list)):
        list = [int(i) for i in Final_list[i]]    
        print(list[0],list[1],list[2],file = f)
    f.close()           

     
    g = graph.Graph(number+1,fileName)
    print("Original TourValue:",g.tourValue())

    g = graph.Graph(number+1,fileName)
    g.swapHeuristic()
    g.tourValue()
    print("Swap TourValue: ",g.tourValue())

    g = graph.Graph(number+1,fileName)
    g.swapHeuristic()
    g.TwoOptHeuristic()
    print("Swap&TwoOpt TourValue: ",g.tourValue())

    g = graph.Graph(number+1,fileName)
    g.Greedy()
    print("Greedy TourValue: ",g.tourValue())

    g = graph.Graph(number+1,fileName)
    g.UniversalGreedy()
    print("my own algorithm: ",g.tourValue())








