#!/usr/bin/python

import sys
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

count = 0

completeSets = []
missingSets = []
fragmentedSets = []
duplicatedSets = []

sets = []
setSizes = []
smallest = 1000 #will be the total number of busco genes

def readArgs():
    count = 0
    for arg in sys.argv:
        if count is not 0:
            file = open(sys.argv[count])

            completeSet = set()
            missingSet = set()
            fragmentedSet = set()
            dupSet = set()

            for line in file:
                if line[0] != "#":

                    splitLine = line.split("\t")
                    if splitLine[1] == 'Complete':
                        completeSet.add(splitLine[0])
                    elif splitLine[1] == 'Duplicated':
                        dupSet.add(splitLine[0])
                    elif splitLine[1] == 'Missing\n':
                        missingSet.add(splitLine[0])
                    elif splitLine[1] == 'Fragmented':
                        fragmentedSet.add(splitLine[0])

            completeSets.append(completeSet)
            missingSets.append(missingSet)
            fragmentedSets.append(fragmentedSet)
            duplicatedSets.append(dupSet)

        count+=1

if len(sys.argv) == 3:

    readArgs()
    venn3(missingSets, (sys.argv[1], sys.argv[2], sys.argv[3]))
    plt.title("Missing BUSCO genes")
    plt.show()

    venn3(completeSets, (sys.argv[1], sys.argv[2], sys.argv[3]))
    plt.title("Complete BUSCO genes")
    plt.show()

    venn3(fragmentedSets, (sys.argv[1], sys.argv[2], sys.argv[3]))
    plt.title("Fragmeneted BUSCO genes")
    plt.show()

    venn3(duplicatedSets, (sys.argv[1], sys.argv[2], sys.argv[3]))
    plt.title("Duplicated BUSCO genes")
    plt.show()

elif len(sys.argv) > 2:


    readArgs()

    print "All 6 genomes\n\n"
    print "Complete Intersection: " + str(len(set.intersection(*completeSets)))
    print "Missing Intersection: " + str(len(set.intersection(*missingSets)))
    print "Fragmented Intersection: " + str(len(set.intersection(*fragmentedSets)))
    print "Duplicated Intersection: " + str(len(set.intersection(*duplicatedSets)))

    count = 0
    while count < len(completeSets):

        print "\nOmitting genome " + str(count + 1) + "\n"

        completed = []
        missing = []
        duplicated = []
        fragmented = []

        i = 0
        while i < len(completeSets):
            if i != count:
                completed.append(completeSets[i])
                missing.append(missingSets[i])
                duplicated1.append(duplicatedSets[i])
                fragmented.append(fragmentedSets[i])
            i+=1

        print "Complete Intersection: " + str(len(set.intersection(*completed)))
        print "Missing Intersection: " + str(len(set.intersection(*missing)))
        print "Fragmented Intersection: " + str(len(set.intersection(*fragmented)))
        print "Duplicated Intersection: " + str(len(set.intersection(*duplicated)))

        count+=1
