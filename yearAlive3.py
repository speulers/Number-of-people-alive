"""
File:  yearAlive3.py
Author:  Bill Bucy
Last updated:  01/31/2018
*******************************************************************************************
Description:  This program is an upgraded version of yearAlive.py and setIntersections.cpp.
Both yearAlive and setIntersections programs have time complexity of O(nlogn) due to the
sorting algorithms they use. yearAlive3 improves upon the time complexity by utilizing an
algorithm that does not rely on sorting. yearAlive3 has time complexity O(n). Further
improvement from setIntersections to yearAlive3 is that yearAlive3 can run with very large
data sets. The testDates.txt has one million rows, which is far more than setIntersections
can handle.
*******************************************************************************************
"""
from time import time
"""
MIN_VAL and MAX_VAL are used as global variables as an easy way to change the parameters
of the program.
"""
MIN_VAL = 1900 
MAX_VAL = 1999

def main():
    """
    inputs:  None
    output:  None
    main function of the program. calls top-level functions. times the program and prints
    result.
    """
    sTime = time()

    bList = getData('testDates.txt')[0]
    dList = getData('testDates.txt')[1]

    mostYears = getMostYears(bList, dList)
    print(mostYears)
    eTime = time()
    tTime = eTime - sTime
    print('Total time: ', tTime)

    return None    

def dataValidation(bYear, dYear):
    """
    inputs:  bYear, dYear
    output:  [bYear, dYear]
    validates data extracted from the file. ensures bYear < dYear and that bYear and dYear
    fall within the parameters of the program (MIN_VAL and MAX_VAL).
    """
    if bYear > dYear:
        print('Error:  birth year > death year for', bYear, dYear, '-> Swapping values.')
        temp = bYear
        bYear = dYear
        dYear = temp
    if bYear < MIN_VAL:
        bYear = MIN_VAL
    if dYear > MAX_VAL:
        dYear = MAX_VAL
    return [bYear, dYear]

def buildList(someList, someInt):
    """
    inputs:  someList, someInt
    output:  someList
    decreases someInt value such that it can be indexed into list someList using the
    smallest possible list length. the index corresponds to the year value.
    """
    someInt -= MIN_VAL
    someList[someInt] += 1
    return someList

def getData(fileName):
    """
    inputs:  fileName
    output: [bList, dList]
    opens the data file and extracts the data, storing it into two lists, bList and dList.
    """
    rangeYears = MAX_VAL - MIN_VAL + 1
    bList = [0]*rangeYears
    dList = [0]*rangeYears
    fi = open(fileName, "r")
    for line in fi:
        bYear, dYear = line.split(',')
        bYear = int(bYear)
        dYear = int(dYear.strip())
        bYear = dataValidation(bYear, dYear)[0]
        dYear = dataValidation(bYear, dYear)[1]
        bList = buildList(bList, bYear)
        dList = buildList(dList, dYear)
    fi.close()
    return [bList, dList]

def getMostYears(bList, dList):
    """
    inputs:  bList, dList
    output:  mostYears
    this is the algorithm that finds the year(s) with the highest occurrence. ties are
    appended to the list mostYears, whereas sole leaders wipe mostYears before appending.
    the algorithm works by increasing count when it encounters bYears and decreasing count
    when it encounters dYears.
    """
    count = 0
    maxCount = 0
    mostYears = 0
    rangeYears = MAX_VAL - MIN_VAL
    for i in range(rangeYears):
        count += bList[i]
        if count == maxCount:
            mostYears.append(i + MIN_VAL)
        elif count > maxCount:
            mostYears = []
            mostYears.append(i + MIN_VAL)
            maxCount = count
        count -= dList[i]
    return mostYears

main()
