#!/usr/bin/python
# ----------------------------------------------------------------------
#  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import cgi
import cgitb
import os
import sys
import time
import pysvn
url = "https://neocortex.numenta.com/svn/Numenta/trunk"

def finished():
    print "</body>"
    sys.exit(0)

cgitb.enable()
form = cgi.FieldStorage()


debug = False

print "Content-Type: text/html"
print

if not debug:
    if not form.has_key("start"):
        print "ERROR: missing start key"
        finished()
    start = int(form["start"].value)

    if not form.has_key("end"):
        print "ERROR: missing end key"
        finished()
    end = int(form["end"].value)

    if form.has_key("detail"):
        detail = int(form["detail"].value)
    else:
        detail = None

    c = pysvn.Client("/Volumes/big/Users/www/.subversion")
else:
    start = 13670
    end = 13693
    detail = 13675
    c = pysvn.Client("/Volumes/big/Users/bsaphir/.stest")


title = "Subversion Log Revision %s through %s" % (start, end)
print "<head>"
print "<title>%s</title>" % title
print '<link rel="stylesheet" type="text/css" href="mystyle.css" />'
print "</head>"
print "<body>"
print "<h2>%s</h2>" % title

debug = False
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


if detail == None:
    logentries = c.log(url, 
                       pysvn.Revision(pysvn.opt_revision_kind.number, start),
                       pysvn.Revision(pysvn.opt_revision_kind.number, end))
else:
    logentries = c.log(url, 
                       pysvn.Revision(pysvn.opt_revision_kind.number, start),
                       pysvn.Revision(pysvn.opt_revision_kind.number, end),
                       discover_changed_paths=True)
                   
if detail is None and len(logentries) == 1:
    detail = logentries[0]["revision"].number
    logentries = c.log(url, 
                       pysvn.Revision(pysvn.opt_revision_kind.number, start),
                       pysvn.Revision(pysvn.opt_revision_kind.number, end),
                       discover_changed_paths=True)

print "<table border=2>"
print """
<thead>
<tr>
  <th>Revision</th>
  <th>Date</th>
  <th>Author</th>
  <th>Message</th>
</tr>
</thead>
<tbody>
"""
for entry in logentries:
    print "<tr>"
    ltime = time.localtime(entry["date"])
    ctime = "%s %02d-%02d %02d:%02d" % (weekdays[ltime.tm_wday], ltime.tm_mon, ltime.tm_mday, ltime.tm_hour, ltime.tm_min)
    if detail is not None and detail == entry["revision"].number:
        print '<td>%s</td>' % entry["revision"].number
        print "<td nowrap>%s</tjd>" % ctime
        print "<td>%s</td>" % entry["author"]
        pathlist = "<br>"
        for p in entry["changed_paths"]:
            pathlist += "%s %s<br>\n" % (p["action"], p["path"])
        print '<td class="detail">%s<br>%s</td>' % (entry["message"].strip(), pathlist)
    else:
        print '<td><a href="delta.py?start=%s&amp;end=%s&amp;detail=%s">%s</a></td>' % (
            start, 
            end, 
            entry["revision"].number, 
            entry["revision"].number)
        print "<td nowrap>%s</tjd>" % ctime
        print "<td>%s</td>" % entry["author"]
        print '<td>%s</td>' % (entry["message"].strip())
    print "</tr>"

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print "</tbody></table>"

finished()

