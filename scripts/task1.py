#!/usr/env/python2.7
import sys
import os
import time

SUCCESS_CODE = '200  OK'

def fanyi(arr):
    dt = {}

    dt['start_time'] = time.ctime( int(arr[0][0:-3]) )
    dt['performance'] = int( arr[1] )
    dt['thread_name'] = arr[5]
    dt['status'] = arr[3] +'  ' + arr[4]
    dt['bytes'] = int(arr[-2])
    dt['latency'] = int(arr[-1])

    return dt

def calc_avg(ls, col):
    sum = 0.0
    for dt in ls:
        sum += dt[col]
    return sum * 1.0 / len(ls)


filename = '../google1.jtl'
fp = open(filename, 'r')
threads = []
success = []

for line in fp.readlines():
    arr = line.split(',')
    dt = fanyi(arr)
    threads.append(dt)
    if dt['status'] == SUCCESS_CODE:
        success.append(dt)
fp.close()

ans = {}
ans['Successful cases'] = len(success)
ans['Failure cases'] = len(threads) - len(success)
ans['Average performance(success)'] = calc_avg(success, 'performance')
ans['Average performance'] = calc_avg(threads, 'performance')
ans['Average latency(success)'] = calc_avg(success, 'latency')
ans['Average latency'] = calc_avg(threads, 'latency')
ans['Average bytes(success)'] = calc_avg(success, 'bytes')
ans['Average bytes'] = calc_avg(threads, 'bytes')

fp = open('google_stat.md','w')
fp.write('<table>')
for key,value in ans.iteritems():
    value = int(value)
    fp.write('<tr><td>**' + key + '**</td><td>' + str(value) + '</td></tr>\n')
fp.write('</table>')
fp.close()


