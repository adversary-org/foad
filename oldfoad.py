#!/usr/bin/env python3

##
# FOAD: Fucked Off Adversarial Degenerates (Fuck Off And Die)
#
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# https://github.com/adversary-org/foad
#
#
# BTC:  1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz
# License:  GNU Public License version 3 (GPLv3)
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Python modules: argparse, random, sys, textwrap
#
# Versions up to 0.4.x developed with Python 2.7.x.  Conversion to
# Python 3 made from version 0.4.2.
#
# A wrapper for foad.py
#
# Old Usage:  oldfoad.py donut foo
#             oldfoad.py outside "FirstName LastName"
#             oldfoad.py king FirstName LastName
#
# Old X-Chat/IRC usage:  /exec -o oldfoad.py donut foo
#                        /exec -o oldfoad.py outside "FirstName LastName"
#                        /exec -o oldfoad.py king FirstName LastName
#
# Calling foad.py in other Python scripts (e.g. Twython for Twitter)
# should be performed with the subprocess module.  Methods for doing
# so are left as an exercise to the reader.
#
# If foad.py is added to site-packages, further help can be obtained
# with pydoc3 (or by running that command in the same directory as the
# script).
#
# Python Documentation help command: pydoc3 foad
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__title__ = "FOAD: Fucked Off Adversarial Degenerates (Fuck Off And Die)"
__license__ = "GNU Public License version 3 (GPLv3)"
__bitcoin__ = "1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz"
__openpgp__ = "0x321E4E2373590E5D"

about = "Wrapper for foad.py to use it the old way."

from foad import __version__
import os
import subprocess
import sys

foad = "./foad.py"
p = os.popen
s = os.system
#p = subprocess.Popen
#s = subprocess.call
#s = subprocess.check_output
sa = sys.argv
l = len(sa)

if l == 1:
    print("""
    %s

    You must specify a type of fuck to give.  Target optional.

    To use run:  oldfoad.py <option> [<target>]
    To test all output run:  oldfoad.py unittest [<target>]
    For random output run:  oldfoad.py random [<target>]

    To see the defined options run:  oldfoad.py list_options

    You should switch to the new version as more options will become
    available.  For more details run:  foad -h

    https://github.com/adversary-org/foad

    %s
    Bitcoin:  %s
    """ % (__title__, __copyright__, __bitcoin__))
    wtf = ""
    target = ""
    #cmd = ""
elif l == 2:
    wtf = sa[1].lower()
    target = ""
    cmd = "%s -f %s" % (foad, wtf)
    s(cmd)
elif l >= 3:
    wtf = sa[1].lower()
    t = []
    for i in range(l - 2):
        t.append(str(sa[i + 2]))
    target = " ".join(t)
    cmd = "%s -f %s -n %s" % (foad, wtf, target)
    s(cmd)
