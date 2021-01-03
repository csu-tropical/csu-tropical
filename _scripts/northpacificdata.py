#Declare Variables
import csv
import sys
filenumber = 1
northeaststormnumber = 0
northweststormnumber = 0
northcentralstormnumber = 0
maxintensity = 0
stormmslp = 0
stormnsd = 0
stormhd = 0
stormmhd = 0
stormace = 0
northeastseasonns = 0
northeastseasonnsd = 0
northeastseasonh = 0
northeastseasonhd = 0
northeastseasonmh = 0
northeastseasonmhd = 0
northeastseasonace = 0
northwestseasonns = 0
northwestseasonnsd = 0
northwestseasonh = 0
northwestseasonhd = 0
northwestseasonmh = 0
northwestseasonmhd = 0
northwestseasonace = 0
ace = 0
mslp = 0
nsformationday = 0
nsformationmonth = 0
nsformationyear = 0
windradii = 0
prevhour = -1
allstats = open('../_data/tc_stats/sixhournorthernhemispherestats.txt', 'a')
allstats.close()
northeastpacificstormstats = open('../_data/tc_stats/northeastpacificstormstats.csv', 'w')
northeastpacificstormstats.write('year,storm_number,name,start_month,start_day,end_month,end_day,latitude,longitude,intensity,mslp,nsd,hd,mhd,ace,basin,storm_charnumber' "\n")

northeastpacificstormstats.close()
northwestpacificstormstats = open('../_data/tc_stats/northwestpacificstormstats.csv', 'w')
northwestpacificstormstats.write('year,storm_number,name,start_month,start_day,end_month,end_day,latitude,longitude,intensity,mslp,nsd,hd,mhd,ace,basin,storm_charnumber' "\n")
northwestpacificstormstats.close()
basinstats = open('../_data/tc_stats/globalstats.txt', 'a')

#Count number of files for basin

import os.path

try:
    onlyfiles = next(os.walk('../_data/tc_stats/North_Pacific'))[2] #dir is your directory path as string
    numfiles = len(onlyfiles)
except StopIteration:
    numfiles = 0

if (numfiles == 0):
    basinstats.write(' '.join(('2021', 'Northeast Pacific', '0', '0', '0', '0', '0', '0', '0', "\n")))
    basinstats.write(' '.join(('2021', 'Northwest Pacific', '0', '0', '0', '0', '0', '0', '0', "\n")))
    basinstats.close()
    sys.exit()

while (filenumber <= numfiles):
    count=1
#Put together Filename
    filename_part1 = '../_data/tc_stats/North_Pacific/np'
    filename_part2 = '2021.csv'
    filename_string = filename_part1 + str(filenumber) + filename_part2

#Open file
    stormfile = open(filename_string)
    stormcsv = csv.reader(stormfile)
    storminfo = list (stormcsv)
    prevhour = -1

#Count number of rows in file
    row_count = len (storminfo)


#Tabulate storm statistics
    while (count <= row_count):
        intensity = storminfo[count-1][8]
        intensity = int(intensity)
        mslp = storminfo[count-1][9]
        mslp = int(mslp)
        category = storminfo[count-1][10]
        windradii = storminfo[count-1][11]
        windradii = int(windradii)
        date_string = storminfo[count-1][2]
        year = date_string[:5]
        month = date_string[5:-4]
        day = date_string[7:-2]
        hour = date_string[9:]
        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        hour = hour * 100

#Only look at rows where system is classifed as ACE generating - also remove any cases where not 34 knot wind radii - to avoid double counting
        if ((category == ' HU' or category == ' TS' or category == ' SS' or category == ' XX' or category == ' TY') and windradii == 34 and (hour == 0 or hour == 600 or hour == 1200 or hour == 1800)):
            if ((intensity >= 35) and (prevhour != hour)):

#Format date variables

                date_string = storminfo[count-1][2]
                year = date_string[:5]
                month = date_string[5:-4]
                day = date_string[7:-2]
                hour = date_string[9:]
                year = int(year)
                month = int(month)
                day = int(day)
                hour = int(hour)
                hour = hour * 100

#Format latitude/longitude variables

                latitude_string = storminfo[count-1][6]
                current_latitude = latitude_string[:4]
                current_latitude = int(current_latitude)/10
                longitude_string = storminfo[count-1][7]
                longitude_code = longitude_string[5:]
                current_longitude = longitude_string[:5]
                if (longitude_code == 'W'):
                    current_longitude = int(current_longitude)/-10
                else:
                    current_longitude = int(current_longitude)/10

#Generate storm intensity info
                if (current_longitude < 0):
                    stormnsd = stormnsd + 0.25
                    northeastseasonnsd = northeastseasonnsd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                else:
                    stormnsd = stormnsd + 0.25
                    northwestseasonnsd = northwestseasonnsd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 64) and (current_longitude < 0)):
                    stormhd = stormhd + 0.25
                    northeastseasonhd = northeastseasonhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 64) and (current_longitude >= 0)):
                    stormhd = stormhd + 0.25
                    northwestseasonhd = northwestseasonhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 96) and (current_longitude < 0)):
                    stormmhd = stormmhd + 0.25
                    northeastseasonmhd = northeastseasonmhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 96) and (current_longitude >= 0)):
                    stormmhd = stormmhd + 0.25
                    northwestseasonmhd = northwestseasonmhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if (maxintensity == 0):
                    maxintensity = intensity
                    stormmslp = mslp
                    nsformationmonth = month
                    nsformationday = day
                    nsformationyear = year
                    formation_latitude = current_latitude
                    formation_longitude = current_longitude
                    if (current_longitude <= -140):
                        northcentralstormnumber = int(northcentralstormnumber) + 1
                        northeastseasonns = northeastseasonns + 1
                    elif (current_longitude < 0):
                        northeaststormnumber = northeaststormnumber + 1
                        northeastseasonns = northeastseasonns + 1
                    else:
                        northweststormnumber = northweststormnumber + 1
                        northwestseasonns = northwestseasonns + 1
                    stormname = storminfo[row_count-1][27]
                    stormname = stormname.strip()
                    if (maxintensity >= 65):
                        if (current_longitude >= 0):
                            northwestseasonh = northwestseasonh + 1
                    if (maxintensity >= 65):
                        if (current_longitude < 0):
                            northeastseasonh = northeastseasonh + 1
                if ((maxintensity < 65) and (intensity >= 65)):
                    if (current_longitude < 0):
                        maxintensity = intensity
                        northeastseasonh = northeastseasonh + 1
                if ((maxintensity < 65) and (intensity >= 65)):
                    if (current_longitude >= 0):
                        maxintensity = intensity
                        northwestseasonh = northwestseasonh + 1
                if ((maxintensity < 96) and (intensity >= 96)):
                    if (current_longitude < 0):
                        maxintensity = intensity
                        northeastseasonmh = northeastseasonmh + 1
                if ((maxintensity < 96) and (intensity >= 96)):
                    if (current_longitude >= 0):
                        maxintensity = intensity
                        northwestseasonmh = northwestseasonmh + 1
                if (maxintensity < intensity):
                    maxintensity = intensity
                if (stormmslp > mslp):
                    stormmslp = mslp
                ace = (intensity * intensity)/10000
                stormace = stormace + ace
                ace = round(ace, 2)
                if (current_longitude < 0):
                    northeastseasonace = northeastseasonace + ace
                if (current_longitude > 0):
                    northwestseasonace = northwestseasonace + ace
                allstats = open('../_data/tc_stats/sixhournorthernhemispherestats.txt', 'a')
                prevhour = hour
                allstats.write(' '.join((str(year), str(month), str(day), str(current_latitude), str(current_longitude), str(intensity), str(mslp), str(category), str(ace), stormname, "\n")))
                allstats.close()
        count = count+1

#Summarize individual storm statistics
    filenumber=filenumber + 1
    stormace = round(stormace, 2)
    storm_abbreviation = storminfo[0][0]
    storm_charnumber = storminfo[0][1]
    storm_charnumber = storm_charnumber.strip()
    if ((maxintensity >0) and ((formation_longitude < 0) and (formation_longitude > -140))):
        northeaststormstats =  open('../_data/tc_stats/northeastpacificstormstats.csv', 'a')
        northeaststormstats.write(','.join((str(year), str(northeaststormnumber), stormname, str(nsformationmonth), str(nsformationday), str(nsdissipationmonth), str(nsdissipationday), \
        str(formation_latitude), str(formation_longitude), str(maxintensity), str(stormmslp), str(stormnsd), str(stormhd), str(stormmhd), str(stormace), str(storm_abbreviation), str(storm_charnumber), "\n")))
        northeaststormstats.close()
    if ((maxintensity >0) and (formation_longitude <= -140)):
        northcentralstormcode = str(northcentralstormnumber)+'C'
        northeaststormstats =  open('../_data/tc_stats/northeastpacificstormstats.csv', 'a')
        northeaststormstats.write(','.join((str(year), northcentralstormcode, stormname, str(nsformationmonth), str(nsformationday), str(nsdissipationmonth), str(nsdissipationday), \
        str(formation_latitude), str(formation_longitude), str(maxintensity), str(stormmslp), str(stormnsd), str(stormhd), str(stormmhd), str(stormace), str(storm_abbreviation), str(storm_charnumber), "\n")))
        northeaststormstats.close()

    if ((maxintensity >0) and (formation_longitude > 0)):
        northweststormstats =  open('../_data/tc_stats/northwestpacificstormstats.csv', 'a')
        northweststormstats.write(','.join((str(year), str(northweststormnumber), stormname, str(nsformationmonth), str(nsformationday), str(nsdissipationmonth), str(nsdissipationday), \
        str(formation_latitude), str(formation_longitude), str(maxintensity), str(stormmslp), str(stormnsd), str(stormhd), str(stormmhd), str(stormace), str(storm_abbreviation), str(storm_charnumber), "\n")))
        northweststormstats.close()

    maxintensity = 0
    nsformationday = 0
    nsformationmonth = 0
    nsformationyear = 0
    stormnsd = 0
    stormhd = 0
    stormmhd = 0
    stormace = 0
northeastseasonace = round (northeastseasonace, 1)
northwestseasonace = round (northwestseasonace, 1)
basinstats = open('../_data/tc_stats/globalstats.txt', 'a')
basinstats.write(' '.join((str(year), 'Northeast Pacific', str(northeastseasonns), str(northeastseasonnsd), str(northeastseasonh), str(northeastseasonhd), str(northeastseasonmh), str(northeastseasonmhd), str(northeastseasonace), "\n")))
basinstats.write(' '.join((str(year), 'Northwest Pacific', str(northwestseasonns), str(northwestseasonnsd), str(northwestseasonh), str(northwestseasonhd), str(northwestseasonmh), str(northwestseasonmhd), str(northwestseasonace), "\n")))
basinstats.close()
