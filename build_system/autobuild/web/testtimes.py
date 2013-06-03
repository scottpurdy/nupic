#!/usr/bin/env python
import re
import sys
import time
import cgi
import cgitb
import os


def finished():
    print "</body>"
    sys.exit(0)


timeReStr = "(\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d):(\d\d)"
timeRe = re.compile(timeReStr)
def parseTime(line):
    matches = timeRe.match(line)
    assert matches
    yr = int(matches.group(1))
    mon = int(matches.group(2))
    day = int(matches.group(3))
    hour = int(matches.group(4))
    min = int(matches.group(5))
    sec = int(matches.group(6))
    t = time.mktime((yr, mon, day, hour, min, sec, 0, 0, 0))
    return t

# old stuff
# ("auto    INFO    Creating source release 'basicplugin-source'", "create basicplugin release"),
# ("release INFO    Building customer basicplugin-source release", "build basicplugin release"),
# ("TEST", "basicplugin"),
# ("=== Test Report", "end of tests"),
# ("auto    INFO    Creating source release 'learningplugin-source'", "create learningplugin release"),
# ("release INFO    Building customer learningplugin-source release", "build learningplugin release"),
# ("TEST", "learningplugin"),
# ("=== Test Report", "end of tests"),
# ("auto    INFO    Creating source release 'tools-source'", "create tools release"),
# ("release INFO    Building customer tools-source release", "build tools release"),
# ("TEST", "toolssource"),
# ("=== Test Report", "end of tests"),
# ("auto    INFO    Creating qa release", "create qa release"),
# ("utils   DEBUG   Copying files", "copy to web server"),


buildSequence = [
("release INFO    Bringing source tree up to date", "svn update"),
("release INFO    Configuring and building trunk", "buildfile gen and configure"),
("build   DEBUG   Building with srcdir", "build"),
("auto    DEBUG   Testing the build", "untar npp release"),
("TEST", "primary"),
("=== Test Report", "end of tests"),
("auto    DEBUG   Running regression tests", "prepare reg tests"),
("TEST", "regression"),
("=== Test Report", "end of tests"),
("release INFO    Creating engineering release", "create eng release"),
("auto    DEBUG   Creating binary release", "create binary release"),
("TEST", "binary-release"),
("=== Test Report", "everything after the binary release"),
("auto    INFO    Overall status", "wrapup"),
("NOMATCH", "")]


def main(filename, sort):
    filename = filename.replace("%2F", "/")

    rev = os.path.dirname(filename)

    log = open(os.path.join("/Volumes/big/www/autobuild", filename))

    print "<table border=2>"
    print """
    <thead>
    <caption><b>Build time report for %s</b></caption>
    <tr>
      <th>Name</th>
      <th>Status</th>
      <th>Time</th>
    </tr>
    </thead>
    """ % rev

    # if tests are done in parallel, we'll see the
    # magic "Starting %d test processes" line later
    parallel = False
    nprocesses = 1


    times = []
    nTests = 0

    # states:
    # We can be in one of three states:
    #  "main" -- going through the sequence defined in buildSequence
    #  "test" -- we're in the middle of a test section.

    sequenceId = 0 # what message we are looking for next

    intest = False
    state = "main"
    # regular expressions for parallel tests
    beginPReStr = "\> running\s+test\s+(\w+)"
    endPReStr = "INFO\s+(\w+):\s+(\w+)"

    # regular expressions for non-parallel tests
    beginReStr = "test\s+INFO\s+Running TEST:\s+(\w+)"
    # endReStr = "QATest\s+INFO\s+Test\s+(\w+)\s+(\w+)\s*"
    endReStr = "QATest\s+INFO\s+Test\s+([^:]+:)\s+(\w+)\s*"

    sequenceRe = re.compile(buildSequence[sequenceId][0])

    parallelRe = re.compile("Starting (\d+) test processes")

    beginRe = re.compile(beginReStr)
    endRe = re.compile(endReStr)


    startTimes = {}

    t1 = 0
    t2 = 0

    # default value for revision in case we don't find it.
    revision = 18247


    for line in log:
        line = line.strip()

        if not parallel:
            s = parallelRe.search(line)
            if s:
                nprocesses = int(s.group(1))
                parallel = True
                beginRe = re.compile(beginPReStr)
                endRe = re.compile(endPReStr)
                startTimes = {}

        l = sequenceRe.search(line)
        if l:

            # print "Found next in sequence: %s<br>" % line
            state = "main"
            t2 = parseTime(line)
            if sequenceId == 0:
                # first in sequence is svn update. get revision number here.
                pass
            else:
                if not buildSequence[sequenceId - 1][0][-4:] == "TEST":
                    times.append((buildSequence[sequenceId - 1][1], "OK", t2 - t1))
            t1 = t2

            # advance to the next in the build sequence
            sequenceId += 1
            if sequenceId == len(buildSequence):
                break
            sequenceRe = re.compile(buildSequence[sequenceId][0])

            # Special action if the next section is a test section.
            if buildSequence[sequenceId][0][-4:] == "TEST":
                # print "Entering test sequence<br>\n"
                startTimes = {}
                # and put ourselves into test search mode
                state = "test"
                firstTest = True
                testtype = buildSequence[sequenceId][1]

                sequenceId += 1
                sequenceRe = re.compile(buildSequence[sequenceId][0])

                # print "beginning tests section. New sequence RE: '%s'" % buildSequence[sequenceId][0]
            continue

        #
        if state == "main":
            # capture all tests for which we found a start but no end
            for t in startTimes:
                times.append(("unknown: %s" % t, "N/A", -1))
            startTimes = {}
            # we'e not searching for tests. just continue
            continue


        if state == "test":
            # Look for the next test
            # print "Looking for test: %s <br>\n" % line
            # import pdb; pdb.set_trace();
            l = beginRe.search(line)
            if l:
                # print "Found beginning of test: %s <br>\n" % line
                # issue record for previous build step
                if firstTest == True:
                    t2 = parseTime(line)
                    times.append((buildSequence[sequenceId - 2][1], "OK", t2 - t1))
                    firstTest = False
                testname = l.group(1)
                t1 = parseTime(line)
                startTimes[testname] = t1

                # print "Found test %s at %s <br>" % (testname, line)
                continue
            l = endRe.search(line)
            if l:
                # print "Found end of test: %s <br>\n" % line
                testname = l.group(2)
                t2 = parseTime(line)
                if testname not in startTimes:
                    print "WARNING: no start for test %s<br>" % testname
                    startTimes[testname] = t2 + 1
                # print "Found end of test '%s': %s<br>" %(testname, line)
                teststatus = l.group(1)
                times.append(("%s: %s" % (testtype, testname), teststatus, t2 - startTimes[testname]))
                del startTimes[testname]
                t1 = t2
                continue

        assert("should not reach here!")


    if sort:
        if sort == 'name':
            times.sort(lambda x, y: -1 if (x[0] < y[0]) else 1)
        else:
            times.sort(lambda x, y: int(x[2] - y[2]), reverse=True)

    # print out all the results
    total_time = 0

    for t in times:
        print "<tr><td>%s</td><td>%s</td><td>%6.1f</td></tr>" % (t[0], t[1], t[2])
        total_time += t[2]
    nTests = len(times)

    print "</table>"
    print "<br>Number of items: %d<br>" % nTests
    print "Total time: %.1f<br>" % total_time
    print "Number of processes: %d<br>" % nprocesses

if __name__ == "__main__":
    cgitb.enable()
    print "Content-Type: text/html"
    print
    print "<head>"
    print "<title>Test times</title>"
    print '<link rel="stylesheet" type="text/css" href="mystyle.css" />'
    print "</head>"
    print "<body>"

    # for key in os.environ:
    #    print "export %s=\"%s\"<br>\n" % (key, os.environ[key])


    form = cgi.FieldStorage()

    if not form.has_key("log"):
        print "ERROR: missing log name"
        finished()

    sort = None
    if form.has_key("sort"):
        sort = form["sort"].value

    main(form["log"].value, sort)
    finished()
