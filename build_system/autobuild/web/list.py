#!/usr/bin/python
# ----------------------------------------------------------------------
#  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

# Warning -- this code is yucky. It is just a quick hack to make it easier to see 
# build status. 

import cgi
import cgitb
import os
import time
baseurl = "http://data.corp.numenta.com/autobuild"

def buildStatusCompare(b1, b2):
    return int(b2.rev) - int(b1.rev)

class buildStatusDir:
    def __init__(self, dir):
        # strip off leading "r"
        self.rev = os.path.basename(dir)
        if self.rev.startswith("r"):
            self.rev = self.rev[1:]
        self.status = dict()
        self.nArchesWithErrors = 0
        for file in os.listdir(dir):
            if file.startswith("status."):
                arch = file[7:]
                self.status[arch] = buildStatus(os.path.join(dir, file))
                if self.status[arch].errors is not None:
                    self.nArchesWithErrors += 1
                if self.status[arch].rev != self.rev:
                    print "ERROR: rev of %s in %s is %s not %s<br>" % (file, dir, self.status[arch].rev, self.rev)
        

class buildStatus:
    def __init__(self, path):
                lines = open(path).readlines()
                self.rev = lines[0].strip()
                self.status = lines[1].strip()
                self.time = lines[2].strip()
                if len(lines) > 3:
                    self.errors = [l.strip() for l in lines[3:]]
                else:
                    self.errors = None

cgitb.enable()
form = cgi.FieldStorage()
if form.has_key("long"):
    long = True
else:
    long = False


print "Content-Type: text/html"
print
print "<head>"
print "<title>Autobuild summary</title>"
print '<link rel="stylesheet" type="text/css" href="mystyle.css" />'
print "</head>"
print "<body>"

# get most recent statuses one at a time because they may have different build numbers

buildStatuses = list()
alldirs = os.listdir(".")
alldirs = sorted(alldirs, reverse=True)
if not long:
    if len(alldirs) > 100:
        alldirs = alldirs[0:100]

for d in alldirs:
    if os.path.isdir(d) and d.startswith("r"):
        buildStatuses.append(buildStatusDir(d))

buildStatuses.sort(buildStatusCompare)

print "<table>"
print """
<thead>
<tr>
  <th>Build</th>
  <th></th>
  <th>Date</th>
  <th>linux64</th>
  <th>linux32</th>
  <th>darwin86</th>
  <th>win32</th>
  <th>errors</th>
</tr>
</thead>
<tbody>
"""

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

nBuilds = len(buildStatuses)
for i in xrange(0, nBuilds):
    b = buildStatuses[i]
    url = "%s/r%s" % (baseurl, b.rev)
    mintime = time.time()
    for a in b.status:
        if float(b.status[a].time) < mintime:
            mintime = float(b.status[a].time)
    ltime = time.localtime(mintime)
    ctime = "%s %02d-%02d %02d:%02d" % (weekdays[ltime.tm_wday], ltime.tm_mon, ltime.tm_mday, ltime.tm_hour, ltime.tm_min)
    
    errors=""
    print '<tr><td><a href="%s">%s</a></td>' % (url, b.rev)
    if i != nBuilds-1:
        prev = int(buildStatuses[i+1].rev) + 1
        print '<td><a href="delta.py?start=%s&amp;end=%s">&Delta;</a></td>' % (prev, b.rev)
    else:
        print '<td></td>'
    print '<td nowrap>%s</td>' % ctime
    for a in ["linux64", "linux32", "darwin86", "win32"]:
        if a in b.status:
            url = "%s/r%s/log.r%s.%s.txt" % (baseurl, b.rev, b.rev, a)
            # b.status[a].status
            if b.status[a].status == "Pass":
                c = "pass"
            else:
                c = "fail"
            print '<td class="%s"><a href="%s">%s</a></td>' % (c, url, a)
            if b.status[a].errors is not None:
                if b.nArchesWithErrors > 1:
                    errors += "%s: " % a
                for e in b.status[a].errors:
                    errors += " %s;" % e
        else:
            print '<td></td>'

    print "<td>%s</td></tr>" % errors
print "</tbody></table>"

print "</body>"

