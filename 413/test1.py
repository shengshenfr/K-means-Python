# -*- coding: utf-8 -*-
"""
k-means algorithm
author :SHEN Sheng
    created on 17/10/2016
"""
import datetime
import time
import random
import sys
from numpy  import *
import matplotlib.pyplot as plt


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
        line[:]= [ float(x) for x in line[:] ]
        if ignore_first_column:
            line = line[1:]
        data.append(line)
    f.close()



    return data


def generate_random_data(nb_objs, nb_attrs, frand = random.random):
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
           somme = somme + pow(x[i] - y[i],5) 
        return pow(somme,1.0/5)

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
            resultat[i][j] = calculerDistance(data[i],centre[j],1)
      
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

def data_set(data,resultat,k):
    for i in xrange(len(data)):
        data[i].append(resultat[i][k])
    return data


   
#if __name__ == "__main__":
#choose k in random or input by user
start=time.clock()
k = 4

data = generate_random_data(500,2)

centre = randomCentre(k,data)
print "centre is " +str(centre)
print '\n'

resultat = [[0 for j in range(k + 1)] for i in range(len(data))]
kmeans(data,k,centre)
print "resultat is " +str(resultat)
print '\n'

nouveau_centre(centre,data,k)
print "nouveau centre is " +str(centre)
    
data_set(data,resultat,k)

write_data(resultat,"resultat.txt")
write_data(data,"out.txt")
write_data(centre,"centre.txt")
#print(len(data))

end=time.clock()
print "the time is" +str(end-start)
numSample = len(data)

print"numSample is " +str(numSample)
print '\n'
dim = len(data[1])-1
print"dimmension is " +str(dim)
print '\n'


mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
if k > len(mark):
    print "Sorry! Your k is too large! "
#print(len(resultat))
#print "resultat: ", resultat[1][4]


# draw all samples
data = mat(data)
resultat = mat(resultat)


plt.figure(1)

for i in xrange(numSample):
    markIndex = int(resultat[i, 4])
    plt.plot(data[i, 0], data[i, 1], mark[markIndex])
plt.title("kmeans clustering")    
plt.axis([0,1,0,1])

plt.show()











