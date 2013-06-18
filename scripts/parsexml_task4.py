#!/usr/env/python2.7

from pyquery import PyQuery as pq

def calc_avg(ls, col):
    sum = 0.0
    for i in xrange(len(ls)):
        sum += int( ls.eq(i).attr(col) )
    return sum * 1.0 / len(ls)

def process(fname):
    fp = open(fname, 'r')
    D = pq(fp.read())
    fp.close()

    print D('httpSample')
    httpSample = D('testResults httpSample')
    print httpSample
    
    ans = {}
    ans['Average performance (ms)'] = calc_avg(httpSample, 't')
    ans['Average latency (ms)'] = calc_avg(httpSample, 'lt')
    ans['Average bytes'] = calc_avg(httpSample, 'by')

    fp = open(fnamei.split('/')[1]+'.md' ,'w')
    fp.write('#### User scenario: Login->Logout\n')
    fp.write('> a Thread Group with 5 threads, Loop Count of 2, and a Ramp-Up period of 5 seconds\n\n')
    fp.write('<table>\n')
    for key,value in ans.iteritems():
        value = int(value)
        fp.write('<tr><td>' + key + '</td><td>' + str(value) + '</td></tr>\n')
    fp.write('</table>')
    fp.close()

process('../login_logout.jtl')
process('../login_weibo.jtl')
