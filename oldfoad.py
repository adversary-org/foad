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
# Version:  0.5.5.2a
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
# Options and notes:
#
# Based on Fuck Off As A Service (FOAAS)
# https://foaas.herokuapp.com/
#
# Includes the same options and many more beyond those.
#
# As the name suggests, most of the output involves the many uses of
# the word "fuck", but some options do not use it.  Running the
# unittest will display the output for all options and show which
# options do not use the word "fuck".
#
# The unittest will display the correct output for almost everything.
#
# The "sherlock" option if it is run with "Sherlock" or "Sherlock
# Holmes" as the target will only produce one result normally, but the
# unittest won't pick that up properly.  The "random" option, however,
# will give the correct output if it happens to hit that option with
# that target.
#
# The acronyms options also does not behave like the main options,
# instead it uses the the target parameter to look up different
# definitions.
#
# Using the acronym option without a target displays an introduction.
# Using the acronym option with a target not specifically addressed
# displays the list of target parameters which can be used with that
# option.  Using any of the listed target parameters will display the
# relevant definition.
#
# There are three options on Latin.  The "priapus" options include
# translation in the "priapus_trans1" and "priapus_trans2" options
# (priapus_trans2 no target contains the translation for priapus no
# target and priapus_trans1 contains the best translation for priapus
# with a target, the other variants are potentially useful).  The
# "omnia" and "vvv" options include translations in comments in the
# source code.
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
__version__ = "0.5.5.2a"
__bitcoin__ = "1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz"
__openpgp__ = "0x321E4E2373590E5D"

about = """Wrapper for foad.py to use it the old way."

import sys
