import urllib.request
import glob
import os
import sys
import datetime
import csv
from urllib.request import Request, urlopen
from urllib.error import  URLError
#...

#Calculate current month, day, hour)
answer = datetime.datetime.now()
answer = str (answer)
currentmonth = answer[5:-19]
currentyear = answer[0:-22]
month = int(currentmonth)
year = int(currentyear)
if(month>6):
    shyear = year + 1
else:
    shyear = year
req = urllib.request.Request('http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
    sys.exit()

#Update count of storms that are already archived (to prevent issues with working best tracks which occasionally happen later)
atlanticstormcount = 0
centralpacificstormcount = 0
nepacificstormcount = 0
nwpacificstormcount = 0
indianstormcount = 0
shstormcount = 0

#North Atlantic
count=1
error=0
while (error == 0):
    if (count > 9):
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bal'
        url_part2 = '.dat'
    else:
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bal0'
        url_part2 = '.dat'
    url_string = url_part1 + str(count) + str(year) + url_part2
    req = Request(url_string)
    try:
        response = urlopen(req)
    except URLError as e:
            error = 1
    else:
        file_string1 = '../_data/tc_stats/Atlantic/al'
        file_string2 = '.csv'
        file_string = file_string1 + str(count) + str(year) + file_string2
        if (count <= atlanticstormcount):
            count = count + 1
        else:
            urllib.request.urlretrieve(url_string, file_string)
            count = count+1

#Central Pacific
count=1
error=0
while (error == 0):
    if (count > 9):
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bcp'
        url_part2 = '.dat'
    else:
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bcp0'
        url_part2 = '.dat'
    url_string = url_part1 + str(count) + str(year) + url_part2
    req = Request(url_string)
    try:
        response = urlopen(req)
    except URLError as e:
            error = 1
    else:
        file_string1 = '../_data/tc_stats/North_Pacific/np'
        file_string2 = '.csv'
        file_string = file_string1 + str(count) + str(year) + file_string2
        if (count <= centralpacificstormcount):
            count = count + 1
        else:
            urllib.request.urlretrieve(url_string, file_string)
            count = count+1

#Northeast Pacific
filenumber=count
count=1
error=0
while (error == 0):
    if (count > 9):
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bep'
        url_part2 = '.dat'
    else:
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bep0'
        url_part2 = '.dat'
    url_string = url_part1 + str(count) + str(year) + url_part2
    req = Request(url_string)
    try:
        response = urlopen(req)
    except URLError as e:
            error = 1
    else:
        file_string1 = '../_data/tc_stats/North_Pacific/np'
        file_string2 = '.csv'
        file_string = file_string1 + str(filenumber) + str(year) + file_string2
        if (count <= nepacificstormcount):
            count = count + 1
            filenumber = filenumber+1
        else:
            urllib.request.urlretrieve(url_string, file_string)
            count = count+1
            filenumber = filenumber+1

#Northwest Pacific
count=1
error=0
while (error == 0):
    if (count > 9):
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bwp'
        url_part2 = '.dat'
    else:
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bwp0'
        url_part2 = '.dat'
    url_string = url_part1 + str(count) + str(year) + url_part2
    req = Request(url_string)
    try:
        response = urlopen(req)
    except URLError as e:
            error = 1
    else:
        file_string1 = '../_data/tc_stats/North_Pacific/np'
        file_string2 = '.csv'
        file_string = file_string1 + str(filenumber) + str(year) + file_string2
        if (count <= nwpacificstormcount):
            count = count + 1
            filenumber = filenumber + 1
        else:
            urllib.request.urlretrieve(url_string, file_string)
            count = count+1
            filenumber = filenumber + 1

#North Indian Ocean
count=1
error=0
while (error == 0):
    if (count > 9):
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bio'
        url_part2 = '.dat'
    else:
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bio0'
        url_part2 = '.dat'
    url_string = url_part1 + str(count) + str(year) + url_part2
    req = Request(url_string)
    try:
        response = urlopen(req)
    except URLError as e:
            error = 1
    else:
        file_string1 = '../_data/tc_stats/North_Indian/ni'
        file_string2 = '.csv'
        file_string = file_string1 + str(count) + str(year) + file_string2
        if (count <= indianstormcount):
            count = count + 1
        else:
            urllib.request.urlretrieve(url_string, file_string)
            count = count+1

#Southern Hemisphere
count=1
error=0
while (error == 0):
    if (count > 9):
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bsh'
        url_part2 = '.dat'
    else:
        url_part1 = 'http://hurricanes.ral.ucar.edu/repository/data/bdecks_open/bsh0'
        url_part2 = '.dat'
    url_string = url_part1 + str(count) + str(shyear) + url_part2
    req = Request(url_string)
    try:
        response = urlopen(req)
    except URLError as e:
            error = 1
    else:
        file_string1 = '../_data/tc_stats/Southern_Hemisphere/sh'
        file_string2 = '.csv'
        file_string = file_string1 + str(count) + str(shyear) + file_string2
        if (count <= shstormcount):
            count = count + 1
        else:
            urllib.request.urlretrieve(url_string, file_string)
            count = count+1
