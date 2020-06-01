#Declare Variables
import csv
import sys
filenumber = 1
stormnumber = 0
maxintensity = 0
stormmslp = 0
stormnsd = 0
stormhd = 0
stormmhd = 0
stormace = 0
seasonns = 0
seasonnsd = 0
seasonh = 0
seasonhd = 0
seasonmh = 0
seasonmhd = 0
seasonace = 0
basin = 'North Indian'
ace = 0
mslp = 0
nsformationday = 0
nsformationmonth = 0
nsformationyear = 0
windradii = 0
allstats = open('../_data/tc_stats/sixhournorthernhemispherestats.txt', 'a')
allstats.close()
northindianstormstats = open('../_data/tc_stats/northindianstormstats.csv', 'w')
northindianstormstats.write('year,storm_number,name,start_month,start_day,end_month,end_day,latitude,longitude,intensity,mslp,nsd,hd,mhd,ace,basin,storm_charnumber' "\n")
northindianstormstats.close()
basinstats = open('../_data/tc_stats/globalstats.txt', 'a')

#Count number of files for basin

import os.path

onlyfiles = next(os.walk('../_data/tc_stats/North_Indian'))[2] #dir is your directory path as string
numfiles = len(onlyfiles)

if (numfiles == 0):
    basinstats.write(' '.join(('2020', basin, '0', '0', '0', '0', '0', '0', '0', "\n")))
    basinstats.close()
    sys.exit()

while (filenumber <= numfiles):
    count=1
#Put together Filename
    filename_part1 = '../_data/tc_stats/North_Indian/ni'
    filename_part2 = '2020.csv'
    filename_string = filename_part1 + str(filenumber) + filename_part2

#Open file
    stormfile = open(filename_string)
    stormcsv = csv.reader(stormfile)
    storminfo = list (stormcsv)

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
        if ((category == ' HU' or category == ' TS' or category == ' SS' or category == ' XX') and windradii == 34 and (hour == 0 or hour == 600 or hour == 1200 or hour == 1800)):
            if (intensity >= 35):

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
                current_longitude = longitude_string[:5]
                current_longitude = int(current_longitude)/10

#Generate storm intensity info
                stormnsd = stormnsd + 0.25
                nsdissipationmonth = month
                nsdissipationday = day
                if (intensity >= 64):
                    nsdissipationmonth = month
                    nsdissipationday = day
                    stormhd = stormhd + 0.25
                if (intensity >= 96):
                    stormmhd = stormmhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if (maxintensity == 0):
                    stormnumber = stormnumber + 1
                    maxintensity = intensity
                    stormmslp = mslp
                    nsformationmonth = month
                    nsformationday = day
                    nsformationyear = year
                    formation_latitude = current_latitude
                    formation_longitude = current_longitude
                    stormname = storminfo[row_count-1][27]
                    stormname = stormname.strip()
                if (maxintensity < intensity):
                    maxintensity = intensity
                if (stormmslp > mslp):
                    stormmslp = mslp
                ace = (intensity * intensity)/10000
                stormace = stormace + ace
                ace = round(ace, 2)
                allstats = open('../_data/tc_stats/sixhournorthernhemispherestats.txt', 'a')
                allstats.write(' '.join((str(year), str(month), str(day), str(current_latitude), str(current_longitude), str(intensity), str(mslp), str(category), str(ace), stormname, "\n")))
                allstats.close()
        count = count+1

#Summarize individual storm statistics
    filenumber=filenumber + 1
    stormace = round(stormace, 2)
    storm_abbreviation = storminfo[0][0]
    storm_charnumber = storminfo[0][1]
    storm_charnumber = storm_charnumber.strip()
    if (maxintensity >0):
        northindianstormstats =  open('../_data/tc_stats/northindianstormstats.csv', 'a')
        northindianstormstats.write(','.join((str(year), str(stormnumber), stormname, str(nsformationmonth), str(nsformationday), str(nsdissipationmonth), str(nsdissipationday), \
        str(formation_latitude), str(formation_longitude), str(maxintensity), str(stormmslp), str(stormnsd), str(stormhd), str(stormmhd), str(stormace), str(storm_abbreviation), str(storm_charnumber), "\n")))
        northindianstormstats.close()

#Tally seasonal statistics
    seasonnsd = seasonnsd + stormnsd
    seasonhd = seasonhd + stormhd
    seasonmhd = seasonmhd + stormmhd
    seasonace = seasonace + stormace
    if (maxintensity > 96):
        seasonmh = seasonmh + 1
        seasonh = seasonh + 1
        seasonns = seasonns + 1
    elif (maxintensity > 64):
        seasonh = seasonh + 1
        seasonns = seasonns + 1
    elif (maxintensity > 34):
        seasonns = seasonns + 1
    maxintensity = 0
    nsformationday = 0
    nsformationmonth = 0
    nsformationyear = 0
    stormnsd = 0
    stormhd = 0
    stormmhd = 0
    stormace = 0

seasonace = round (seasonace, 1)
basinstats = open('../_data/tc_stats/globalstats.txt', 'a')

basinstats.write(' '.join((str(year), basin, str(seasonns), str(seasonnsd), str(seasonh), str(seasonhd), str(seasonmh), str(seasonmhd), str(seasonace), "\n")))
basinstats.close()
