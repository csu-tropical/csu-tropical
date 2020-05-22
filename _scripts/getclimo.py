import datetime
import csv
# Calculate current month and day
answer = datetime.datetime.now()
answer = str (answer)
currentmonth = answer[5:-19]
currentday = answer[8:-16]
monthday = currentmonth+currentday
monthday = int(monthday);
monthday = str(monthday);
# Find current month and day in text file
climostats = open('../_data/tc_stats/seasonal_cycle.csv', 'r')
climocsv = csv.reader(climostats)
climoinfo = list (climocsv)
rowcount = len (climoinfo)
count = 1
while (count<=rowcount):
    date = climoinfo[count-1][0]
    date = str(date)
    # Update today climo file to have climatological values for today
    if (date == monthday):
        allstats = open('../_data/tc_stats/today_climo.txt', 'w')
        allstats.write(' '.join((climoinfo[count-1][1], climoinfo[count-1][2], climoinfo[count-1][3], climoinfo[count-1][4], climoinfo[count-1][5], climoinfo[count-1][6], climoinfo[count-1][7], \
                                 climoinfo[count-1][8], climoinfo[count-1][9], climoinfo[count-1][10], climoinfo[count-1][11], climoinfo[count-1][12], climoinfo[count-1][13], climoinfo[count-1][14], \
                                 climoinfo[count-1][15], climoinfo[count-1][16], climoinfo[count-1][17], climoinfo[count-1][18], climoinfo[count-1][19], climoinfo[count-1][20], climoinfo[count-1][21], \
                                 climoinfo[count-1][22], climoinfo[count-1][23], climoinfo[count-1][24], climoinfo[count-1][25], climoinfo[count-1][26], climoinfo[count-1][27], climoinfo[count-1][28], \
                                 climoinfo[count-1][29], climoinfo[count-1][30], climoinfo[count-1][31], climoinfo[count-1][32], climoinfo[count-1][33], climoinfo[count-1][34], climoinfo[count-1][35], \
                                 climoinfo[count-1][36], climoinfo[count-1][37], climoinfo[count-1][38], climoinfo[count-1][39], climoinfo[count-1][40], climoinfo[count-1][41], climoinfo[count-1][42], "\n")))
        allstats.close()
    count = count + 1
climostats.close()
