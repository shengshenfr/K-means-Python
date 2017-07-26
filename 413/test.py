# -*- coding: utf-8 -*-
"""
k-means algorithm
author :SHEN Sheng
    created on 17/10/2016
"""
import random
import sys
from numpy  import *
import datetime
import time


def read_data(filename, skip_first_line = False, ignore_first_column = False):
    '''
    Loads data from a csv file and returns the corresponding list.
    All data are expected to be floats, except in the first column.
    
    @param filename: csv file name.
    
    @param skip_first_line: if True, the first line is not read.
        Default value: False.
    
    @param ignore_first_column: if True, the first column is ignored.
        Default value: False.
    
    @return: a list of lists, each list being a row in the data file.
        Rows are returned in the same order as in the file.
        They contains floats, except for the 1st element which is a string
        when the first column is not ignored.
    '''
    
    f = open(filename,'r')
    if skip_first_line:
        f.readline()
    
    data = []
    for line in f:
        line = line.split(",")
        line[:] = [ float(x) for x in line[:] ]
        if ignore_first_column:
            line = line[1:]
        data.append(line)
    f.close()


    return data


def generate_random_data(frand = random.random):
    '''
    Generates a matrix of random data.
    
    @param frand: the fonction used to generate random values.
        It defaults to random.random.
        Example::

            import random
            generate_random_data(5, 6, lambda: random.gauss(0, 1))
    
    @return: a matrix with nb_objs rows and nb_attrs+1 columns. The 1st
        column is filled with line numbers (integers, from 1 to nb_objs).
    '''
    nb_objs = int(raw_input('input ligne:'))
    nb_attrs = int(raw_input('input colonne:'))

    data = []
    for i in range(nb_objs):
        #line = [i+1]
        #for j in range(numAtt):
        #    line.append(frand())
        #line = [i+1] + map(lambda x: frand(), range(nb_attrs))
        line = map(lambda x: frand(), range(nb_attrs))
        data.append(line)
    return(data)

def write_data(data, filename):
    '''
    Writes data in a csv file.

    @param data: a list of lists

    @param filename: the path of the file in which data is written.
        The file is created if necessary; if it exists, it is overwritten.
    '''
    # If you're curious, look at python's module csv instead, which offers
    # more powerful means to write (and read!) csv files.
    f = open(filename, 'w')
    for item in data:
        f.write(','.join([repr(x) for x in item]))
        f.write('\n')
    f.close()




    '''
    calculate the distance between two points
    type = 1: distance Euclien
    type = 2: distance Manhattan
    type = 3: distance Minkowski, avec index = 5
    '''
def calculerDistance(x,y,type):
    
    somme = 0
    if type == 0:
        for i in xrange(len(x)):
            somme = somme + pow(x[i] - y[i], 2)
        return pow(somme, 0.5)
    
    if  type == 1:
        for i in xrange(len(x)):
            somme = somme + abs(x[i] - y[i])
        return somme
    
    if type == 2:
        for i in xrange(len(x)):
           somme = somme + pow(abs(x[i] - y[i]),100) 
        return pow(somme,1.0/100)
    
# choose k numbers of centers from data in random
def randomCentre(k,data):
    
    centre = []
    ordre = []
    i = 0
    while (i<k):
        x = random.randint(0,len(data)-1)
        if (x not in ordre):
            ordre.append(x)
            centre.append(data[x])
            i += 1
    return centre
 

# choose k number of centers before k number  
def before_k_Centre(k,data):
    
    centre = []
    for i in xrange(k):
        centre.append(data[i])
    return centre




# kmeans algorithm: for each point find the minimum valer of point
def kmeans(data, k, centre):

    for i in xrange(len(data)):
        for j in xrange(len(centre)):
            
            # calculer the distance of two points
            # reserver in the list 'resultat'
            resultat[i][j] = calculerDistance(data[i],centre[j],2)
      
        minimum = resultat[i].index(min(resultat[i][:len(resultat[0]) - 1]))
        
        if resultat[i][k] != minimum:
            resultat[i][k] = minimum
    
    return resultat

# refresh centers of each group after clustering
def nouveau_centre(centre,data,k):
    for i in xrange(k):
        
        #count all the point in each cluster 
        total_point = 0 

        for j in xrange(len(resultat)): 
            if resultat[j][k] == i: 
                total_point +=  1 
                for m in xrange(len(data[0])): 
                    centre[i][m] = centre[i][m] + data[j][m]
#            print centre[i]

        # calculer the mean of each center as the new centers
        for x in xrange(len(data[0])):


            centre[i][x] = centre[i][x] / total_point
#        print "centre is " + str(centre[i])

    return centre

def choisir_K(argv):
    
    if argv[1] == 'randomk':
        k = random.randint(2,kMax)
        print "random k =" + str(k)
        return k

    else:
        k = int(argv[1])
        print "use k =" + str(k)
        return k

def data_set(data,resultat,k):
    for i in xrange(len(data)):
        data[i].append(resultat[i][k])
    return data
       

    
#if __name__ == "__main__":
#choose k in random or input by user
start=time.clock()
kMax =6
if len(sys.argv)<3:
    print "break" + sys.argv[0]
    exit(0)
    
k = choisir_K(sys.argv)

#generater the date in random or read data of document
data = []
if sys.argv[2] == 'randomdata':
    data = generate_random_data()
else:
    data = read_data(sys.argv[2])

#print "data is " +str(data)
#write_data(data, "out.txt")
#print(data)
print '\n'


# generater the centers by random in the data or choose before k lines of the data as centers 
if sys.argv[3] == 'randomCentre':
    centre = randomCentre(k,data)
    print "generater centres random"
else :
    centre = before_k_Centre(k,data)

print "centre is " +str(centre)
print '\n'

#define un list for stock the cluster
resultat = [[0 for j in range(k + 1)] for i in range(len(data))]

# when arguments have 4 , output the result
if len(sys.argv) == 4:
    kmeans(data,k,centre)

    #print "resultat is " +str(resultat)
    print '\n'

    nouveau_centre(centre,data,k)
    print "nouveau centre is " +str(centre)
    
    data_set(data,resultat,k)
#test the data IRIS   
write_data(data,"iris_result.txt")


end=time.clock()
print "the time fo programme is" +str(end-start) +"s"
