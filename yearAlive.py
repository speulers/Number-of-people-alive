"""
File:  yearAlive.py
Author:  Bill Bucy
Description:  A program that determines the year(s) with the most people alive
"""

fi = open("data.txt", "r")

years_arr = []

for line in fi:
    b_year, d_year = line.split(',')
    b_year = int(b_year)
    d_year = int(d_year.strip())
    if b_year > d_year:
        temp = b_year
        b_year = d_year
        d_year = temp
        print('Error:  birth year > death year for', line, '-> Swapping values.')
    years_arr.append([b_year, 1])
    years_arr.append([d_year, -1])
    
fi.close()

years_arr.sort()

count = 0
max_count = 0
most_years = []
most_range = ''

for index in range(len(years_arr)):
    if count == max_count:
        most_range = str(years_arr[index - 1][0]) + '-' + str(years_arr[index][0])
        most_years.append(most_range)
    elif count > max_count:
        most_years = []
        most_range = str(years_arr[index - 1][0]) + '-' + str(years_arr[index][0])
        most_years.append(most_range)
        max_count = count
    count += years_arr[index][1]
    
print(most_years)
