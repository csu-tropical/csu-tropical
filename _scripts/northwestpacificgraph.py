import datetime
import csv

def datestdtojd (stddate):
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)

#Calculate current year, month, day, hour)
answer = datetime.datetime.now()
answer = str (answer)
currentyear = answer[0:4]
currentmonth = answer[5:-19]
currentday = answer[8:-16]
currenthour = answer[11:-13]
juliandayindex = datestdtojd(currentyear + '-' + currentmonth + '-' + currentday) -1

currentmonth = int(currentmonth)
currentday = int(currentday)
currenthour = int(currenthour)

#If it is January 1st, reset observed northwestpacific ACE'
if (currentmonth==1):
	if(currentday==1):
		os.remove('../_data/tc_stats/northwestpacificacetodate.txt', 'w')

# Get current ACE
globalstatstable = open('../_data/tc_stats/globalstats.txt', 'r')
globalcsv = csv.reader(globalstatstable, delimiter=' ')
globalarray = list(globalcsv)
currentace = globalarray[2][9]
globalstatstable.close()

#Open .csv file with seasonal cycle data
seasonalcycletable = open('../_data/tc_stats/seasonal_cycle.csv', 'r')
seasonalcyclecsv = csv.reader(seasonalcycletable, delimiter=',')
seasonalcyclearray = list(seasonalcyclecsv)
seasonalcycletable.close()

#Open .csv file with ace to date
basinacetodatetable = open('../_data/tc_stats/northwestpacificacetodate.txt', 'r')
basinacetodatecsv = csv.reader(basinacetodatetable, delimiter=',')
basinacetodatearray = list(basinacetodatecsv)
basinacetodatetable.close()

basinacetodatetable = open('../_data/tc_stats/northwestpacificacetodate.txt', 'w')
count = 0
while (count < juliandayindex):
#Append observed data for as many days as there have been this year
#If the current hour is the last time of the day that the script is run, then update ACE to date file for basin
	basinacetodatetable.write(''.join((seasonalcyclearray[count][43], "-", currentyear, ",", basinacetodatearray[count][1], "\n")))
	count = count + 1
basinacetodatetable.write(''.join((seasonalcyclearray[count][43], "-", currentyear, ",", currentace, "\n")))
basinacetodatetable.close()
#If it is March 1st, add a day for February 29 - works until 2020
#	if (currentmonth==3):
#		if(currentday==1):
#Open additional files necessary to create ACE to date .csv file for graphing
basinacetodatevsclimotable = open('../_data/tc_stats/northwestpacificacetodatevsclimo.csv', 'w')
basinacetodatevsclimotable.write(''.join(('Date,Observed,Climatology',"\n")))
#Open .csv file with basin ACE to date
basinacetodatetable = open('../_data/tc_stats/northwestpacificacetodate.txt', 'r')
basincsv = csv.reader(basinacetodatetable, delimiter=',')
basinarray = list(basincsv)
basindays = len(basinarray)
count = 0
while (count < 366):
#Append observed data for as many days as there have been this year
	if (count < basindays):
		basinacetodatevsclimotable.write(''.join((seasonalcyclearray[count][43], "-", currentyear, ",", basinarray[count][1], ",", seasonalcyclearray[count][21], "\n")))
		count = count + 1
#Append remainder of climatological curve
	else:
		basinacetodatevsclimotable.write(''.join((seasonalcyclearray[count][43], "-", currentyear, ",,",  seasonalcyclearray[count][21], "\n")))
		count = count + 1
basinacetodatevsclimotable.close()
