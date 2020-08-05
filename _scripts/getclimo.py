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
climocount = 0
while (count<=rowcount):
    date = climoinfo[count-1][0]
    date = str(date)
    # Update today climo file to have climatological values for today
    if (date == monthday):
        climocount = count-1
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
# Read in the global stats
globalstatstable = open('../_data/tc_stats/globalstats.txt', 'r')
globalcsv = csv.reader(globalstatstable, delimiter=' ')
globalarray = list(globalcsv)
globalstatstable.close()
# Write out the combined stats and climo
globalstats = open('../_data/tc_stats/globalstats.csv', 'w')
globalstats.write("basin,ns,nsclimo,nsd,nsdclimo,h,hclimo,hd,hdclimo,mh,mhclimo,mhd,mhdclimo,ace,aceclimo\n")
count = 0
while (count<=5):
    climoidx = count * 7
    globalstats.write(''.join((globalarray[count][1], " ", globalarray[count][2], ",", globalarray[count][3], ",", climoinfo[climocount][1+climoidx], ",", \
                               globalarray[count][4], ",", climoinfo[climocount][2+climoidx], ",", globalarray[count][5], ",", climoinfo[climocount][3+climoidx], ",", \
                               globalarray[count][6], ",", climoinfo[climocount][4+climoidx], ",", globalarray[count][7], ",", climoinfo[climocount][5+climoidx], ",", \
                               globalarray[count][8], ",", climoinfo[climocount][6+climoidx], ",", globalarray[count][9], ",", climoinfo[climocount][7+climoidx], "\n")))
    if (count == 3):
        # Sum up northern Hemisphere
        globalstats.write(''.join(("Northern Hemisphere", ",", str(int(globalarray[0][3])+int(globalarray[1][3])+int(globalarray[2][3])+int(globalarray[3][3])), ",", \
                                   f'{(float(climoinfo[climocount][1])+float(climoinfo[climocount][8])+float(climoinfo[climocount][15])+float(climoinfo[climocount][22])):.1f}', ",", \
                                   f'{(float(globalarray[0][4])+float(globalarray[1][4])+float(globalarray[2][4])+float(globalarray[3][4])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][2])+float(climoinfo[climocount][9])+float(climoinfo[climocount][16])+float(climoinfo[climocount][23])):.1f}', ",", \
                                   str(int(globalarray[0][5])+int(globalarray[1][5])+int(globalarray[2][5])+int(globalarray[3][5])), ",", \
                                   f'{(float(climoinfo[climocount][3])+float(climoinfo[climocount][10])+float(climoinfo[climocount][17])+float(climoinfo[climocount][24])):.1f}', ",", \
                                   f'{(float(globalarray[0][6])+float(globalarray[1][6])+float(globalarray[2][6])+float(globalarray[3][6])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][4])+float(climoinfo[climocount][11])+float(climoinfo[climocount][18])+float(climoinfo[climocount][25])):.1f}', ",", \
                                   str(int(globalarray[0][7])+int(globalarray[1][7])+int(globalarray[2][7])+int(globalarray[3][7])), ",", \
                                   f'{(float(climoinfo[climocount][5])+float(climoinfo[climocount][12])+float(climoinfo[climocount][19])+float(climoinfo[climocount][26])):.1f}', ",", \
                                   f'{(float(globalarray[0][8])+float(globalarray[1][8])+float(globalarray[2][8])+float(globalarray[3][8])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][6])+float(climoinfo[climocount][13])+float(climoinfo[climocount][20])+float(climoinfo[climocount][27])):.1f}', ",", \
                                   f'{(float(globalarray[0][9])+float(globalarray[1][9])+float(globalarray[2][9])+float(globalarray[3][9])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][7])+float(climoinfo[climocount][14])+float(climoinfo[climocount][21])+float(climoinfo[climocount][28])):.1f}', "\n")))

    if (count == 5):
        # Sum up southern Hemisphere
        globalstats.write(''.join(("Southern Hemisphere", ",", str(int(globalarray[4][3])+int(globalarray[5][3])), ",", \
                                   f'{(float(climoinfo[climocount][29])+float(climoinfo[climocount][36])):.1f}', ",", \
                                   f'{(float(globalarray[4][4])+float(globalarray[5][4])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][30])+float(climoinfo[climocount][37])):.1f}', ",", \
                                   str(int(globalarray[4][5])+int(globalarray[5][5])), ",", \
                                   f'{(float(climoinfo[climocount][31])+float(climoinfo[climocount][38])):.1f}', ",", \
                                   f'{(float(globalarray[4][6])+float(globalarray[5][6])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][32])+float(climoinfo[climocount][39])):.1f}', ",", \
                                   str(int(globalarray[4][7])+int(globalarray[5][7])), ",", \
                                   f'{(float(climoinfo[climocount][33])+float(climoinfo[climocount][40])):.1f}', ",", \
                                   f'{(float(globalarray[4][8])+float(globalarray[5][8])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][34])+float(climoinfo[climocount][41])):.1f}', ",", \
                                   f'{(float(globalarray[4][9])+float(globalarray[5][9])):.1f}', ",", \
                                   f'{(float(climoinfo[climocount][35])+float(climoinfo[climocount][42])):.1f}', "\n")))

    count = count + 1
globalstats.close()
