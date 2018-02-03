"""
File:  yearAlive3_1.py
Author:  Bill Bucy
Last updated:  02/03/2018
********************************************************************************
Description:  This program reads birth and death years from a .txt file and
returns the year(s) in which the most people were alive. Extracting the data
requires an algorithm that runs in O(n) time. Once the data is extracted, the
algorithm that finds the most years alive runs in O(1) time.
********************************************************************************
Update 0202201800:  changed bList and dList in main() so that getData is only
called once. This reduces runtime by decreasing the constant of proportionality,
k in T(n) = kn + c
********************************************************************************
Update 0202201801:  removed bList and dList, combining into myList. removed
buildList() function. this reduced runtime and also eliminated about 15 lines of
code.
********************************************************************************
Update 0203201800:  added data validation in the event a birth year falls after
the MAX_VAL or if a death year falls before the MIN_VAL.
********************************************************************************
"""
from time import time
"""
MIN_VAL and MAX_VAL are used as global variables as an easy way to change the
parameters of the program.
"""
MIN_VAL = 1900 
MAX_VAL = 1999

def main():
    """
    inputs:  None
    output:  None
    main function of the program. calls top-level functions. times the program
    and prints result.
    """
    sTime = time()

    myList = getData('testDates.txt')

    mostYears = getMostYears(myList)
    print(mostYears)
    eTime = time()
    tTime = eTime - sTime
    print('Total time: ', tTime)

    return None    

def dataValidation(bYear, dYear):
    """
    inputs:  bYear, dYear
    output:  [bYear, dYear]
    validates data extracted from the file. ensures bYear < dYear and that bYear
    and dYear fall within the parameters of the program (MIN_VAL and MAX_VAL).
    """
    if bYear > dYear:
        print('Error:  birth year > death year for', bYear, dYear, \
              '-> Swapping values.')
        temp = bYear
        bYear = dYear
        dYear = temp
    if bYear < MIN_VAL:
        bYear = MIN_VAL
    if dYear > MAX_VAL:
        dYear = MAX_VAL

    return [bYear, dYear]

def getData(fileName):
    """
    inputs:  fileName
    output: [bList, dList]
    opens the data file and extracts the data, storing it into two lists, bList
    and dList.
    """
    myList = [[0]*(MAX_VAL + 1), [0]*(MAX_VAL + 1)]
    fi = open(fileName, 'r')
    for line in fi:
        bYear, dYear = line.split(',')
        bYear = int(bYear)
        dYear = int(dYear.strip())
        if bYear > MAX_VAL or dYear < MIN_VAL:
            continue
        bYear, dYear = dataValidation(bYear, dYear)

        myList[0][bYear] += 1
        myList[1][dYear] += 1
    fi.close()
    return myList

def getMostYears(someList):
    """
    inputs:  bList, dList
    output:  mostYears
    this is the algorithm that finds the year(s) with the highest occurrence.
    ties are appended to the list mostYears, whereas sole leaders wipe mostYears
    before appending.the algorithm works by increasing count when it encounters
    bYears and decreasing count when it encounters dYears.
    """
    count = 0
    maxCount = 0
    mostYears = []

    for i in range(MIN_VAL, MAX_VAL + 1):
        count += someList[0][i]
        if count == maxCount:
            mostYears.append(i)
        elif count > maxCount:
            mostYears = []
            mostYears.append(i)
            maxCount = count
        count -= someList[1][i]
    return mostYears

main()
