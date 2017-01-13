#include <iostream>
#include <fstream>													//for ifstream
#include <string>													//for substr
#include <stdlib.h>													//for qsort & atoi


using namespace std;

int getBegin(std::string b)											//converts a string into an integer representing birth year
{
	
	int pos = b.length() - 10;
	std::string bString = b.substr(pos, 4);
	int bInt = atoi(bString.c_str());
	return bInt;
}

int getEnd(std::string e)											//converts a string into an integer representing death year
{
	int pos = e.length() - 4;
	std::string eString = e.substr(pos, 4);
	int eInt = atoi(eString.c_str());
	return eInt;
}

int compare (const void * m, const void * n)						//used for qsort
{
	return (*(int*)m - *(int*)n);
}
int main()
{
	
	int x = 0;
	string line;
	int dataSize = 0;
	ifstream dataFile("data.txt");
	while (getline(dataFile, line))
	{
		dataSize++;													//a single pass of the file determines the size of lArr
	}
	string lArr[dataSize];
	int bArr[dataSize];
	int eArr[dataSize];
	int fixArr = 0;
	int z = 2 * dataSize;
	dataFile.close();
	ifstream datFile("data.txt");
	while (getline(datFile, line))									//extracts the data from the file data.txt line by line
	{
		lArr[x] = line;												//and stores it into lArr, an array of strings
		x++;
	}
	dataFile.close();
	for (int k = 0; k < dataSize; k++)
	{
		bArr[k] = getBegin(lArr[k]);
		eArr[k] = getEnd(lArr[k]);
		if (bArr[k] > eArr[k])										//throws an error if a birth year was greater than its death year
		{
			cout << "Error!  Birth year > death year!  Line "  << k + 1 << '\n';
			fixArr = bArr[k];
			bArr[k] = eArr[k];
			eArr[k] = fixArr;
			cout << "New data set includes range " << bArr[k] << " - " << eArr[k] << '\n';
		}
	}
	qsort(bArr, dataSize, sizeof(int), compare);					//sorts array of birth years
	qsort(eArr, dataSize, sizeof(int), compare);					//sorts array of death years
	int arr[2][z];													
	int bHead = 0;
	int eHead = 0;
	int i = 0;

	while (bArr[dataSize - 1] != 0 && eArr[dataSize - 1] != 0)		//merges the two arrays into a single, two-dimensional array
	{																//this while loop combined with one below it is a merge sort
		if (bArr[bHead] <= eArr[eHead])								//since the two arrays are already sorted, it requires only a single pass
		{
			arr[0][i] = bArr[bHead];
			bArr[bHead] = 0;
			bHead++;
			arr[1][i] = 1;											//when a birth year is added to arr[0][i], the value 1 is assigned to arr[1][i]
		}															
		else
		{
			arr[0][i] = eArr[eHead];
			eArr[eHead] = 0;
			eHead++;
			arr[1][i] = -1;											//when a death year is added to arr[0][i], the value -1 is assigned to arr[1][i]
		}
		i++;
	}
	while (eArr[dataSize - 1] != 0)									//merges the remaining elements of eArr into arr
	{																//since eArr represents death years bArr[dataSize - 1] <= eArr[dataSize -1]
		arr[0][i] = eArr[eHead];									//thus bArr is "emptied" first
		eArr[eHead] = 0;
		eHead++;
		arr[1][i] = -1;
		i++;
	}

	int maxArr[dataSize][2];
	int tie = 0;
	int count = 0;
	int max = 0;
	for (int y = 1; y < z; y++)										//this is the algorithm that finds the set of values representing the year(s) with the most people alive
	{
		count += arr[1][y - 1];										//it keeps a running total of the second row of array arr
		if (count == max)											//all values of this running total that are the maximum are the years with the most people alive
		{
			tie++;													
			maxArr[tie][0] = arr[0][y - 1];							//when the running total equals the former maximum, the current range is added to the next row of maxArr
			maxArr[tie][1] = arr[0][y];								//that way ties can be included in the final result
		}
		else
		{
			if (count > max)										//if the running total exceeds the former running total or tied values
			{
				max = count;
				tie = 0;											//the tie counter is reset
				maxArr[tie][0] = arr[0][y - 1];						//and the current range is stored in the first row of maxArr
				maxArr[tie][1] = arr[0][y];
			}
		}
		
	}																//after this algorithm makes a single pass, the first (tie + 1) amount of rows will be the range of years with the most people alive
																	
	for (int o = 0; o <= tie; o++)
	{
		cout << maxArr[o][0] << " - " << maxArr[o][1] << '\n';		//this loop prints a list of year ranges representing the most people alive
	}
	return 0;
}
