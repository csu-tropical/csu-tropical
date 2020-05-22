import datetime
import csv
#Calculate current month, day, hour)
answer = datetime.datetime.now()
answer = str (answer)
currentmonth = answer[5:-19]
currentday = answer[8:-16]
currenthour = answer[11:-13]
currentmonth = int(currentmonth)
currentday = int(currentday)
currenthour = int(currenthour)
#If it is January 1st, reset observed Atlantic ACE'
if (currentmonth==1):
	if(currentday==1):
		os.remove('../_data/tc_stats/northernhemisphereacetodate.txt', 'w')
#If the current hour is the last time of the day that the script is run, then update ACE to date file for basin
if (currenthour>=18):
	basinacetodatetable = open('../_data/tc_stats/northernhemisphereacetodate.txt', 'a')
	globalstatstable = open('../_data/tc_stats/globalstats.txt', 'r')
	globalcsv = csv.reader(globalstatstable, delimiter=' ')
	globalarray = list(globalcsv)
	value = float(globalarray[0][9])+float(globalarray[1][9])+float(globalarray[2][9])+float(globalarray[3][9])
	value = str(value)
	basinacetodatetable.write(value + '\n')
#If it is March 1st, add a day for February 29 - works until 2020
	if (currentmonth==3):
		if(currentday==1):
			basinacetodatetable.write(value + '\n')
	globalstatstable.close()
	basinacetodatetable.close()
#Open additional files necessary to create ACE to date .csv file for graphing
	basinacetodatevsclimotable = open('../_data/tc_stats/northernhemisphereacetodatevsclimo.csv', 'w')
	basinacetodatevsclimotable.write(' '.join(('Date,Observed,Climatology',"\n")))
#Open .csv file with basin ACE to date
	basinacetodatetable = open('../_data/tc_stats/northernhemisphereacetodate.txt', 'r')
	basincsv = csv.reader(basinacetodatetable, delimiter=' ')
	basinarray = list(basincsv)
	basindays = len(basinarray)
#Open .csv file with seasonal cycle data
	seasonalcycletable = open('../_data/tc_stats/seasonal_cycle.csv', 'r')
	seasonalcyclecsv = csv.reader(seasonalcycletable, delimiter=',')
	seasonalcyclearray = list(seasonalcyclecsv)
	count = 0
	while (count < 366):
#Append observed data for as many days as there have been this year
		if (count < basindays):
			basinacetodatevsclimotable.write(''.join((seasonalcyclearray[count][43], ",", basinarray[count][0], ",", seasonalcyclearray[count][44], "\n")))
			count = count + 1
#Append remainder of climatological curve
		else:
			basinacetodatevsclimotable.write(''.join((seasonalcyclearray[count][43], ",,",  seasonalcyclearray[count][44], "\n")))
			count = count + 1
	basinacetodatevsclimotable.close()
