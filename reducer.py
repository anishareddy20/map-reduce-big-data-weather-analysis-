#!/usr/bin/env python
import sys
import operator

current_year = None

max_count = 0
min_count = 0

avg_max = 0
avg_min = 0

hottest = []
coldest = []

max = (-9999,'','')
min = (99999,'','')

for line in sys.stdin:
    line = line.strip().split(',')

    date = line[0]
    year = date[:4]
    id = line[1]
    metric = line[2]
    value = line[3]

    try:
        value = int(value)
    except ValueError:
        continue
    
    if current_year is None:
        current_year = year
    
    if current_year != year:
        print 'Year: %s' % current_year
        print 'Average TMAX: %s' % (avg_max * 1.0 / max_count)
        print 'Average TMIN: %s' % (avg_min * 1.0 / min_count)

        print 'Hottest Day: day: %s | val: %s | loc: %s' %(hottest[0][2], hottest[0][0], hottest[0][1])
        print 'Coldest Day: day: %s | val: %s | loc: %s' %(coldest[0][2], coldest[0][0], coldest[0][1])

        print 'Hottest Stations %s' % ([x[1] for x in hottest])
        print 'Hottest Station Values %s' % ([x[0] for x in hottest])
        print 'Coldest Stations %s' % ([x[1] for x in coldest])
        print 'Coldest Station Values %s' % ([x[0] for x in coldest])

        print '-----------------------------------------------------'


        current_year = year

        max_count = 0
        min_count = 0

        avg_max = 0
        avg_min = 0

        hottest = []
        coldest = []

    if metric == 'TMAX':
        avg_max += value
        max_count += 1
        if max[0] < value:
            max = (value,id,date)

        hottest.append((value,id,date))

        if len(hottest) > 5:
            hottest = sorted(hottest, key=operator.itemgetter(0), reverse=True)
            hottest.pop(len(hottest) - 1)
    
    elif metric == 'TMIN':
        avg_min += value
        min_count += 1
        if min[0] > value:
            min = (value,id,date)

        coldest.append((value,id,date))

        if len(coldest) > 5:
            coldest = sorted(coldest, key=operator.itemgetter(0))
            coldest.pop(len(coldest) - 1)






print 'Year: %s' % current_year
print 'Average TMAX: %s' % (avg_max * 1.0 / max_count)
print 'Average TMIN: %s' % (avg_min * 1.0 / min_count)

print 'Hottest Day: day: %s | val: %s | loc: %s' %(hottest[0][2], hottest[0][0], hottest[0][1])
print 'Coldest Day: day: %s | val: %s | loc: %s' %(coldest[0][2], coldest[0][0], coldest[0][1])

print 'Hottest Stations %s' % ([x[1] for x in hottest])
print 'Hottest Station Values %s' % ([x[0] for x in hottest])
print 'Coldest Stations %s' % ([x[1] for x in coldest])
print 'Coldest Station Values %s' % ([x[0] for x in coldest])

print '============================================================================'

print 'Max TMAX: %s | Station: %s' % (max[0],max[1])
print 'Min TMIN: %s | Station: %s' % (min[0],min[1])
	
