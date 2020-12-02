#Declare Variables
import csv
import sys
filenumber = 1
southpacificstormnumber = 0
southindianstormnumber = 0
maxintensity = 0
stormmslp = 0
stormnsd = 0
stormhd = 0
stormmhd = 0
stormace = 0
southpacificseasonns = 0
southpacificseasonnsd = 0
southpacificseasonh = 0
southpacificseasonhd = 0
southpacificseasonmh = 0
southpacificseasonmhd = 0
southpacificseasonace = 0
southindianseasonns = 0
southindianseasonnsd = 0
southindianseasonh = 0
southindianseasonhd = 0
southindianseasonmh = 0
southindianseasonmhd = 0
southindianseasonace = 0
ace = 0
mslp = 0
nsformationday = 0
nsformationmonth = 0
nsformationyear = 0
windradii = 0
allstats = open('../_data/tc_stats/sixhoursouthernhemispherestats.txt', 'w')
allstats.write( "YEAR" ' ' "MONTH" ' ' "DAY" ' ' "LATITUDE" ' ' "LONGITUDE" ' ' "MAX_WIND" ' ' "MSLP" ' ' "CATEGORY" ' ' "ACE" ' ' "STORM_NAME" "\n")
southpacificstormstats = open('../_data/tc_stats/southpacificstormstats.csv', 'w')
southpacificstormstats.write('year,storm_number,name,start_month,start_day,end_month,end_day,latitude,longitude,intensity,mslp,nsd,hd,mhd,ace,basin,storm_charnumber' "\n")
southpacificstormstats.close()

southindianstormstats = open('../_data/tc_stats/southindianstormstats.csv', 'w')
southindianstormstats.write('year,storm_number,name,start_month,start_day,end_month,end_day,latitude,longitude,intensity,mslp,nsd,hd,mhd,ace,basin,storm_charnumber' "\n")
southindianstormstats.close()
basinstats = open('../_data/tc_stats/globalstats.txt', 'a')

#Count number of files for basin

import os.path

onlyfiles = next(os.walk('../_data/tc_stats/Southern_Hemisphere'))[2] #dir is your directory path as string
numfiles = len(onlyfiles)

if (numfiles == 0):
    basinstats.write(' '.join(('2021', 'South Indian', '0', '0', '0', '0', '0', '0', '0', "\n")))
    basinstats.write(' '.join(('2021', 'South Pacific', '0', '0', '0', '0', '0', '0', '0', )))
    basinstats.close()
    sys.exit()

while (filenumber <= numfiles):
    count=1
#Put together Filename
    filename_part1 = '../_data/tc_stats/Southern_Hemisphere/sh'
    filename_part2 = '2021.csv'
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
        if ((category == ' HU' or category == ' TS' or category == ' SS' or category == ' XX' or category == ' TY') and windradii == 34 and (hour == 0 or hour == 600 or hour == 1200 or hour == 1800)):
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
                current_latitude = int(current_latitude)/-10
                longitude_string = storminfo[count-1][7]
                longitude_code = longitude_string[5:]
                current_longitude = longitude_string[:5]
                if (longitude_code == 'W'):
                    current_longitude = int(current_longitude)/-10
                else:
                    current_longitude = int(current_longitude)/10

#Generate storm intensity info
                if ((current_longitude > 30) and (current_longitude < 135)):
                    stormnsd = stormnsd + 0.25
                    southindianseasonnsd = southindianseasonnsd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                else:
                    stormnsd = stormnsd + 0.25
                    southpacificseasonnsd = southpacificseasonnsd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 64) and ((current_longitude > 30) and (current_longitude < 135))):
                    stormhd = stormhd + 0.25
                    southindianseasonhd = southindianseasonhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 64) and ((current_longitude > 135) or (current_longitude < 0))):
                    stormhd = stormhd + 0.25
                    southpacificseasonhd = southpacificseasonhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 96) and ((current_longitude > 30) and (current_longitude < 135))):
                    stormmhd = stormmhd + 0.25
                    southindianseasonmhd = southindianseasonmhd + 0.25
                    nsdissipationmonth = month
                    nsdissipationday = day
                if ((intensity >= 96) and ((current_longitude > 135) or (current_longitude < 0))):
                    stormmhd = stormmhd + 0.25
                    southpacificseasonmhd = southpacificseasonmhd + 0.25
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
                    if ((current_longitude > 135) or (current_longitude < 0)):
                        southpacificstormnumber = southpacificstormnumber + 1
                        southpacificseasonns = southpacificseasonns + 1
                    else:
                        southindianstormnumber = southindianstormnumber + 1
                        southindianseasonns = southindianseasonns + 1
                    stormname = storminfo[row_count-1][27]
                    stormname = stormname.strip()
                    if (maxintensity >= 65):
                        if ((current_longitude > 135) or (current_longitude < 0)):
                            southpacificseasonh = southpacificseasonh + 1
                    if (maxintensity >= 65):
                        if ((current_longitude > 30) and (current_longitude < 135)):
                            southindianseasonh = southindianseasonh + 1
                if ((maxintensity < 65) and (intensity >= 65)):
                    if ((current_longitude > 135) or (current_longitude < 0)):
                        maxintensity = intensity
                        southpacificseasonh = southpacificseasonh + 1
                if ((maxintensity < 65) and (intensity >= 65)):
                    if ((current_longitude > 30) and (current_longitude < 135)):
                        if (intensity >= 96):
                            southindianseasonmh = southindianseasonmh + 1
                        maxintensity = intensity
                        southindianseasonh = southindianseasonh + 1
                if ((maxintensity < 96) and (intensity >= 96)):
                    if ((current_longitude > 135) or (current_longitude < 0)):
                        maxintensity = intensity
                        southpacificseasonmh = southpacificseasonmh + 1
                if ((maxintensity < 96) and (intensity >= 96)):
                    if ((current_longitude > 30) and (current_longitude < 135)):
                        maxintensity = intensity
                        southindianseasonmh = southindianseasonmh + 1
                if (maxintensity < intensity):
                    maxintensity = intensity
                if (stormmslp > mslp):
                    stormmslp = mslp
                ace = (intensity * intensity)/10000
                stormace = stormace + ace
                ace = round(ace, 2)
                if ((current_longitude > 135) or (current_longitude < 0)):
                    southpacificseasonace = southpacificseasonace + ace
                if ((current_longitude > 30) and (current_longitude < 135)):
                    southindianseasonace = southindianseasonace + ace
                allstats = open('../_data/tc_stats/sixhoursouthernhemispherestats.txt', 'a')
                allstats.write(' '.join((str(year), str(month), str(day), str(current_latitude), str(current_longitude), str(intensity), str(mslp), str(category), str(ace), stormname, "\n")))
                allstats.close()
        count = count+1

#Summarize individual storm statistics
    filenumber=filenumber + 1
    stormace = round(stormace, 2)
    storm_abbreviation = storminfo[0][0]
    storm_charnumber = storminfo[0][1]
    storm_charnumber = storm_charnumber.strip()

    if ((maxintensity >0) and ((formation_longitude > 135) or (formation_longitude < 0))):
        southpacificstormstats =  open('../_data/tc_stats/southpacificstormstats.csv', 'a')
        southpacificstormstats.write(','.join((str(year), str(southpacificstormnumber), stormname, str(nsformationmonth), str(nsformationday), str(nsdissipationmonth), str(nsdissipationday), \
        str(formation_latitude), str(formation_longitude), str(maxintensity), str(stormmslp), str(stormnsd), str(stormhd), str(stormmhd), str(stormace), str(storm_abbreviation), str(storm_charnumber), "\n")))
        southpacificstormstats.close()

    if ((maxintensity >0) and ((formation_longitude > 30) and (formation_longitude < 135))):
        southindianstormstats =  open('../_data/tc_stats/southindianstormstats.csv', 'a')
        southindianstormstats.write(','.join((str(year), str(southindianstormnumber), stormname, str(nsformationmonth), str(nsformationday), str (nsdissipationmonth), str(nsdissipationday), \
        str(formation_latitude), str(formation_longitude), str(maxintensity), str(stormmslp), str(stormnsd), str(stormhd), str(stormmhd), str(stormace), str(storm_abbreviation), str(storm_charnumber), "\n")))
        southindianstormstats.close()

    maxintensity = 0
    nsformationday = 0
    nsformationmonth = 0
    nsformationyear = 0
    stormnsd = 0
    stormhd = 0
    stormmhd = 0
    stormace = 0
southpacificseasonace = round (southpacificseasonace, 1)
southindianseasonace = round (southindianseasonace, 1)
basinstats = open('../_data/tc_stats/globalstats.txt', 'a')
basinstats.write(' '.join((str(year), 'South Indian', str(southindianseasonns), str(southindianseasonnsd), str(southindianseasonh), str(southindianseasonhd), str(southindianseasonmh), str(southindianseasonmhd), str(southindianseasonace), "\n")))
basinstats.write(' '.join((str(year), 'South Pacific', str(southpacificseasonns), str(southpacificseasonnsd), str(southpacificseasonh), str(southpacificseasonhd), str(southpacificseasonmh), str(southpacificseasonmhd), str(southpacificseasonace), )))
basinstats.close()
