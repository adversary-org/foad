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
# Version:  0.7.1.12
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
# Previous versions might have worked with Python 3.0 and 3.1 (I don't
# know for sure, I never checked), but with the inclusion of the
# argparse module this is now lo longer possible (if it ever was).
#
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
# There are four options in Latin.  The "priapus" options include
# translation in the "priapus_trans1" and "priapus_trans2" options
# (priapus_trans2 no target contains the translation for priapus no
# target and priapus_trans1 contains the best translation for priapus
# with a target, the other variants are potentially useful).  The
# "custode", "omnia" and "vvv" options include translations in
# comments in the source code.
#
# There are at least three options which depend on the encoding being
# UTF-8 (those being "custode", "omnia" and "linus").  If the
# copyright symbols peppered throughout the script don't display
# properly then there's a good chance that those options won't either.
#
#
# The script now uses argparse to handle input, which means the order
# of the input types can be switched around since it is the flag which
# determines how the input is initially handled and not the order of
# the arguments.  However, it is now essential when using arguments
# with two or more words (e.g. names) to place them in quotation marks
# as in the examples.
#
# Usage:  foad.py -f donut -n foo
#         foad.py -f outside --name "FirstName LastName"
#         foad.py --fuck king --name "FirstName LastName"
#         foad.py -n Veronica --fuck chainsaw
#         foad.py -f field3 -n Bob -s Kate -e "Some stuff."
#
# The old method of calling the script will still work, but only for
# the argument types available at this point (i.e. --fuck and --name).
# Newer argument types (e.g. --extra and --sender) will not be
# available through the old method.  When using this old method the
# order in which the options are specified is important.
#
# Old Usage:  foad.py donut foo
#             foad.py outside "FirstName LastName"
#             foad.py king FirstName LastName
#
# Old X-Chat/IRC usage:  /exec -o foad.py donut foo
#                        /exec -o foad.py outside "FirstName LastName"
#                        /exec -o foad.py king FirstName LastName
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
# Command line help and hints: foad.py -h
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyrightu__ = "Copyright © Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__copyrighth__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__title__ = "FOAD: Fucked Off Adversarial Degenerates (Fuck Off And Die)"
__stitle__ = "FOAD"
__license1__ = "GNU General Public License version 3 (GPLv3)"
__license2__ = "Do What The Fuck You Want To, But It's Not My Fault Public License version 1 (WTFNMFPLv1)"
__version__ = "0.7.1.12"
__bitcoin__ = "1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz"
__openpgp__ = "0x321E4E2373590E5D"

import argparse
import locale
import random
import sys
import textwrap

if locale.getlocale()[1] == "UTF-8":
    __copyright__ = __copyrightu__
elif locale.getdefaultlocale()[1] == "UTF-8":
    __copyright__ = __copyrightu__
elif locale.getpreferredencoding() == "UTF-8":
    __copyright__ = __copyrightu__
else:
    try:
        __copyright__ = __copyrighth__
    except locale.Error:
        __copyright__ = __copyrighta__


about = """
{0}
Version {1}
{2}
License:  {3}
          {4}

For instructions run:  {5} -h

Contact:  {6} {7}
Bitcoin:  {8}
""".format(__title__, __version__, __copyright__, __license1__, __license2__, sys.argv[0], __author__, __openpgp__, __bitcoin__)

version = "{0} (foad.py) version {1}".format(__stitle__, __version__)

lx = len(sys.argv)

if lx == 2 and sys.argv[1].startswith("-") is False:
    sys.argv.insert(1, "-f")
elif lx == 3 and sys.argv[1].startswith("-") is False and sys.argv[2].startswith("-") is False:
    sax = []
    sax.append(sys.argv[0])
    sax.append("-f")
    sax.append(sys.argv[1])
    sax.append("-n")
    sax.append(sys.argv[2])
    sys.argv = sax
elif lx >= 4 and sys.argv[1].startswith("-") is False and sys.argv[2].startswith("-") is False:
    sax = []
    sax.append(sys.argv[0])
    sax.append("-f")
    sax.append(sys.argv[1])
    sax.append("-n")
    sax.append(" ".join(sys.argv[2:lx]))
    sys.argv = sax

parser = argparse.ArgumentParser(
    prog="foad.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__title__, epilog=textwrap.dedent("""\
        You MUST place any parameter of more than one word in
        quotation marks.

        Can only be used with the old calling method with the
        equivalent of -f and -n.  If additional parameters are used
        (e.g. --extra or --sender), then the current method MUST be
        used.

        For more help run:  pydoc3 foad

        https://github.com/adversary-org/foad

        Bitcoin:  {0}

    {1}
    {2}
    """.format(__bitcoin__, version, __copyright__)))
parser.add_argument("-f", "--fuck", help="One word, indicates type of fuck to give, run foad.py -f list_options to see possible flags.", action="store", required=False)
parser.add_argument("-n", "--name", help="Name of target, more than one word must be in quotation marks.", action="store", required=False)
parser.add_argument("-s", "--sender", help="Used to specify the sender, usually within the context of some particular phrase, more than one word must be in quotation marks.", action="store", required=False)
parser.add_argument("-e", "--extra", help="Additional comment to append to output, more than one word must be in quotation marks.  Sometimes used to enhance an existing response rather than append text.", action="store", required=False)
parser.add_argument("-c", "--cite", help="Enter anything here to include a citation if it is relevent.", action="store", required=False)
# The next two can wait as they're already covered by -f and -h, both are causing problems at the moment:
# parser.add_argument("-l", "--list_options", help="Lists the explicit variations (the same as: -f list_options)", action="store", required=False)
# parser.add_argument("-V", "--version", help="Print the version number.", action=print(version), required=False)

if len(sys.argv) > lx:
    la = len(sys.argv)
else:
    la = lx
#la = lx

sa = []
for a in sys.argv:
    if a.startswith("-") is False:  # input can't begin with a hyphen anyway.
        sa.append(a)

l = len(sa)

args = parser.parse_args()

if args.fuck is None:
    wtf = ""
else:
    wtf = args.fuck.lower()

if args.name is None:
    target = ""
else:
    target = args.name

if args.sender is None:
    sender = ""
else:
    sender = args.sender

if args.extra is None:
    extra = ""
else:
    extra = args.extra

if args.cite is None:
    cite = ""
#elif args.cite.lower() == "yes" or "y" or "true" or "1":
#    cite = "citation"
else:
    cite = "citation"

lt = len(target)
ls = len(sender)
le = len(extra)

class fuck:
    def a(self):
        if lt == 0 and le == 0:
            msg = "Fuckin' A!"
        elif lt == 0 and le > 0:
            msg = "Fuckin' A!  {0}".format(extra)
        elif lt > 0 and le == 0:
            msg = "{0}, fuckin' A!".format(target)
        elif lt > 0 and le > 0:
            msg = "{0}, fuckin' A!  {1}".format(target, extra)
        else:
            msg = "{0}, fuckin' A!  {1}  -- {2}".format(target, extra, sender)
        print(msg)

    def about(self):
        if lt == 0:
            msg = textwrap.fill("Messages and other information to be displayed interactively.  As with the acronym option, the target parameters are used to call each message.  A non-existent target parameter will produce a list of available options.", 72)
        elif target.lower() == "adversary":
            msg = "Organised Adversary"
        elif target.lower() == "atitle":
            msg = __title__
        elif target.lower() == "author":
            msg = __author__
        elif target.lower() == "bitcoin":
            msg = __bitcoin__
        elif target.lower() == "contact":
            msg = "See the following 'foad.py about' parameters: email, gpg key, irc and domain."
        elif target.lower() == "copyright":
            msg = __copyright__
        elif target.lower() == "domain":
            msg = "http://www.adversary.org/"
        elif target.lower() == "donations":
            msg = "If you find this script useful, please donate to the Bitcoin address included."
        elif target.lower() == "email":
            msg = "ben@adversary.org"
        elif target.lower() == "encryption":
            msg = "My GPG key is included for a reason, we should all be encrypting everything all the time."
        elif target.lower() in "gpg key":
            msg = __openpgp__
        elif target.lower() == "irc":
            msg = "Hasimir on freenode.net"
        elif target.lower() == "options":
            msg = "Number of defined options:  {0}".format(lc)
        elif target.lower() == "pirate":
            msg = "http://www.pirateparty.org.au/"
        elif target.lower() == "twitter":
            msg = "Use this script with the Twython Tools scripts or anything which can call it and post the output."
        elif target.lower() in "twython tools":
            msg = "https://github.com/adversary-org/twython-tools"
        elif target.lower() == "version":
            msg = __version__
        elif target.lower() == "website":
            msg = "https://github.com/adversary-org/foad"
        else:
            msg = textwrap.fill("Target parameters: adversary, atitle, author, bitcoin, contact, copyright, domain, donations, email, encryption, gpg key, irc, options, pirate, twitter, twython, version, website.", 72)
        print(msg)

    def acronym(self):
        if lt == 0:
            msg = textwrap.fill("Acronyms and backronyms; use the target parameter to choose which one.  To view the target parameters run: foad.py -f acronym -n x", 72)
        elif target.lower() == "fubar":
            msg = "FUBAR: Fucked Up Beyond All Recognition"
        elif target.lower() == "carnal":
            msg = """FUCK: For Unlawful Carnal Knowledge
      Actually a backronym and urban myth on the origin of the word fuck."""
        elif target.lower() == "bond":
            msg = """FUCK: Freddy Uncle Charlie Katie
      A backronym used by Ian Fleming to avoid censors in one of the James Bond novels."""
        elif target.lower() == "die":
            msg = "FOAD: Fuck Off And Die"
        elif target.lower() == "right":
            msg = "FROAD: Fuck Right Off And Die"
        elif target.lower() == "title":
            msg = "FOAD: Fucked Off Adversarial Degenerates"  # Also a backronym.
        elif target.lower() == "figjam":
            msg = "FIGJAM: Fuck I'm Good, Just Ask Me"
        elif target.lower() == "cunt":
            msg = """CUNT: Caring Understanding Nineties Type
      A response to SNAG."""
        elif target.lower() == "foaas":
            msg = """FOAAS: Fuck Off As A Service
        The API which led to this script since that API is not consistently
        maintained."""
        elif target.lower() == "lmfao":
            msg = "LMFAO: Laughing My Fucking Arse Off"
        elif target.lower() == "snag":
            msg = """SNAG: Sensitive New Age Guy
      See also: CUNT"""
        elif target.lower() == "snafu":
            msg = "SNAFU: Situation Normal: All Fucked Up"
        else:
            msg = textwrap.fill("Target parameters: bond, carnal, cunt, die, figjam, foaas, fubar, lmfao, right, snafu, snag, title.", 72)
        print(msg)

    def agree(self):
        if lt == 0:
            msg = "Abso-fucking-lutely!"
        elif lt == 0 and le > 0:
            msg = "Abso-fucking-lutely!  {0}".format(extra)
        elif lt > 0 and le == 0:
            msg = "Abso-fucking-lutely {0}!".format(target)
        elif lt > 0 and le > 0:
            msg = "Abso-fucking-lutely {0}!  {1}".format(target, extra)
        else:
            msg = "Abso-fucking-lutely {0}!  {1}  -- {2}".format(target, extra, sender)
        print(msg)

    def amaze(self):
        if lt == 0:
            msg = "That was fucking amazing!"
        elif lt > 0 and le == 0:
            msg = "{0}, that was fucking amazing!".format(target)
        else:
            msg = "{0}, that was fucking amazing!  {1}".format(target, extra)
        print(msg)

    def apple(self):
        if lt == 0 and le == 0 and ls == 0:
            msg = "No you fucking can't do it your way!  We don't give a fuck if it's better, you do it our fucking way or you fuck off!"
        elif lt > 0 and le == 0 and ls == 0:
            msg = "No {0}, you fucking can't do it your way!  We don't give a fuck if it's better, you do it our fucking way or you fuck off!".format(target)
        elif lt > 0 and le > 0 and ls == 0:
            msg = "No {0}, you fucking can't do it your way!  We don't give a fuck if it's better, you do it our fucking way or you fuck off!  {1}".format(target, extra)
        elif lt > 0 and le == 0 and ls > 0:
            msg = "No {0}, you fucking can't do it your way!  We don't give a fuck if it's better, you do it our fucking way or you fuck off!  -- {1}".format(target, sender)
        else:
            msg = "No {0}, you fucking can't do it your way!  We don't give a fuck if it's better, you do it our fucking way or you fuck off!  {1}  -- {2}".format(target, extra, sender)
        print(msg)

    def ballmer(self):
        if lt == 0 and le == 0 and ls == 0:
            msg = "Ballmer Notes: This option requires the first target specified with --name and the second (usually a company or organisation) with --extra (sender optional).  For a plural version on --name use ballmers on --fuck."
        elif lt > 0 and le == 0 and ls == 0:
            msg = "Fucking {0} is a fucking pussy.  I'm going to bury that guy, I have done it before and I will do it again.  I'm going to fucking kill {1}.".format(target, target)
        elif lt > 0 and le > 0 and ls == 0:
            msg = "Fucking {0} is a fucking pussy.  I'm going to bury that guy, I have done it before and I will do it again.  I'm going to fucking kill {1}.".format(target, extra)
        elif lt > 0 and le == 0 and ls > 0:
            msg = "Fucking {0} is a fucking pussy.  I'm going to bury that guy, I have done it before and I will do it again.  I'm going to fucking kill {1}.  -- {2}".format(target, target, sender)
        elif lt > 0 and le > 0 and ls > 0:
            msg = "Fucking {0} is a fucking pussy.  I'm going to bury that guy, I have done it before and I will do it again.  I'm going to fucking kill {1}.  -- {2}".format(target, extra, sender)
        print(msg)

    # consider making a female variant of this.

    def ballmers(self):
        if lt == 0 and le == 0 and ls == 0:
            msg = "Plural Ballmer Notes: This option requires the first targets specified with --name in quotation marks (e.g. 'name1 and name2' or 'name1, name2 and name3') and the second (usually a company or organisation) with --extra (sender optional)."
        elif lt > 0 and le == 0 and ls == 0:
            msg = "Fucking {0} are fucking pussies.  I'm going to bury those guys, I have done it before and I will do it again.  I'm going to fucking kill {1}.".format(target, target)
        elif lt > 0 and le > 0 and ls == 0:
            msg = "Fucking {0} are fucking pussies.  I'm going to bury those guys, I have done it before and I will do it again.  I'm going to fucking kill {1}.".format(target, extra)
        elif lt > 0 and le == 0 and ls > 0:
            msg = "Fucking {0} are fucking pussies.  I'm going to bury those guys, I have done it before and I will do it again.  I'm going to fucking kill {1}.  -- {2}".format(target, target, sender)
        elif lt > 0 and le > 0 and ls > 0:
            msg = "Fucking {0} are fucking pussies.  I'm going to bury those guys, I have done it before and I will do it again.  I'm going to fucking kill {1}.  -- {2}".format(target, extra, sender)
        print(msg)

    def bbm(self):
        if lt == 0:
            msg = "Big bad motherfucker."
        elif lt == 0 and ls > 0:
            msg = "{0} is a big bad motherfucker.".format(sender)
        elif lt > 0 and ls > 0:
            msg = "{0}, {1} is a big bad motherfucker.".format(target, sender)
        else:
            msg = "{0}, {1} is a big bad motherfucker.  {2}".format(target, sender, extra)
        print(msg)

    def caniuse(self):
        if lt == 0 and ls == 0 and le == 0:
            msg = "Can I Use Notes: This option requires the tool/object be specified with --extra and is a two-parter rolled into one command.  Currently requires --name, --extra and --sender."
        elif lt > 0 and ls > 0 and le > 0:
            msg = """{0}, it's {1} here, can I use {2}?  ...  Can you use {3}?  Fuck no, {4}!  You cannot fucking use {5}!""".format(sender, target, extra, extra, target, extra)
        print(msg)

    def cango(self):
        if lt == 0:
            msg = "They can go and fuck themselves."
        elif lt > 0 and ls > 0:
            msg = "Tell {0} that {1} said they can go and fuck themselves.".format(target, sender)
        else:
            msg = "{0} can go and fuck themselves.".format(target)
        print(msg)

    def cbf(self):
        if lt == 0:
            msg = "I can't be fucked!"
        else:
            msg = "{0}, I can't be fucked!".format(target)
        print(msg)

    def chainsaw(self):
        if lt == 0:
            msg = "Fuck me gently with a chainsaw.  Do I look like Mother Teresa?"
        else:
            msg = "Fuck me gently with a chainsaw, {0}.  Do I look like Mother Teresa?".format(target)
        print(msg)

    def chainsawe(self):
        if lt == 0:
            msg = "Fuck me gently with a chainsaw!  Do I look like Mother Teresa?!"
        else:
            msg = "Fuck me gently with a chainsaw, {0}!  Do I look like Mother Teresa?!".format(target)
        print(msg)

    def chainsaws(self):
        if lt == 0:
            msg = "Fuck me gently with a chainsaw!"
        else:
            msg = "Fuck me gently with a chainsaw, {0}!".format(target)
        print(msg)

    def cfm(self):
        if lt == 0:
            msg = "Come fuck me."
        else:
            msg = "{0}, come fuck me.".format(target)
        print(msg)

    def cluster(self):
        if lt == 0:
            msg = "It's a total cluster-fuck!"
        else:
            msg = "{0}, it's a total cluster-fuck!".format(target)
        print(msg)

    def clustera(self):
        if lt == 0:
            msg = "It's an almighty cluster-fuck!"
        else:
            msg = "{0}, it's an almighty cluster-fuck!".format(target)
        print(msg)

    def cocksuck(self):
        if lt == 0:
            msg = "Fuck you, you fucking cocksucker!"
        else:
            msg = "Fuck you {0}, you fucking cocksucker!".format(target)
        print(msg)

    def compleat(self):
        if lt == 0:
            msg = "I might be a cunt, but I'm not a complete and utter fucking cunt."
        else:
            msg = "I might be a cunt, {0}, but I'm not a complete and utter fucking cunt.".format(target)
        print(msg)

    def cracked(self):
        if lt == 0:
            msg = "You are fucking cracked!"
        else:
            msg = "{0}, you are fucking cracked!".format(target)
        print(msg)

    def cunt(self):
        if lt == 0:
            msg = "Fuck you, you complete and utter fucking cunt!"
        else:
            msg = "Fuck you {0}, you complete and utter fucking cunt!".format(target)
        print(msg)

    def cunts(self):
        if lt == 0:
            msg = "Fuck you, you complete and utter fucking cunts!"
        else:
            msg = "Fuck you {0}, you complete and utter fucking cunts!".format(target)
        print(msg)

    def cuntz(self):
        if lt == 0:
            msg = "Fuck all those complete and utter fucking cocksuckers and cunts!"
        else:
            msg = "Fuck the {0}, they're all complete and utter fucking cocksuckers and cunts!".format(target)
        print(msg)

    def custode(self):
        if lt == 0:
            msg = "Sed quis custodiet ipsos futūtor?"
            # But who will guard the fucker(s)?
        else:
            msg = "{0}, quis custodiet ipsos futūtor?".format(target)
        print(msg)

    def deadwood(self):
        if lt == 0:
            msg = "You fucking cocksucker!"
        else:
            msg = "{0}, you're a fucking cocksucker!".format(target)
        print(msg)

    def denial(self):
        if lt == 0:
            msg = "I didn't fucking do it!"
        else:
            msg = "{0}, I didn't fucking do it!".format(target)
        print(msg)

    def disbelief(self):
        if lt == 0:
            msg = "Un-fucking-believable!"
        else:
            msg = "Un-fucking-believable {0}!".format(target)
        print(msg)

    def does(self):
        if lt == 0:
            msg = "Does it look like I give a fuck?"
        else:
            msg = "{0}, does it look like I give a fuck?".format(target)
        print(msg)

    def donut(self):
        if lt == 0:
            msg = "Go and take a flying fuck at a rolling donut."
        else:
            msg = "{0}, go and take a flying fuck at a rolling donut.".format(target)
        print(msg)

    def doodle(self):
        msg = "Fuck-a-doodle-doo!"
        print(msg)

    def dorothy(self):
        if lt == 0:
            msg = "Too fucking busy and vice versa."  # Dorothy Parker
        else:
            msg = "{0}, I'm too fucking busy and vice versa.".format(target)
        print(msg)

    def duck(self):
        if lt == 0:
            msg = "Fuck a duck!"
        else:
            msg = "{0}, fuck a duck!".format(target)
        print(msg)

    def english(self):
        if lt == 0:
            msg = "English motherfucker!  Do you speak it?!"
        else:
            msg = "English motherfucker!  Do you speak it {0}?!".format(target)
        print(msg)

    def every1(self):
        if lt == 0:
            msg = "Everyone's fucked!"
        else:
            msg = "{0}, everyone's fucked!".format(target)
        print(msg)

    def every2(self):
        if lt == 0:
            msg = "Everything's fucked!"
        else:
            msg = "{0}, everything's fucked!".format(target)
        print(msg)

    def exorcist(self):
        if lt == 0:
            msg = "Your mother sucks cocks in Hell!"
        else:
            msg = "Your mother sucks cocks in Hell, {0}!".format(target)
        print(msg)

    def fascinating(self):
        if lt == 0:
            msg = "Fascinating story, in what chapter do you shut the fuck up?"
        else:
            msg = "Fascinating story, {0}, in what chapter do you shut the fuck up?".format(target)
        print(msg)

    def ffs(self):
        if lt == 0:
            msg = "For fuck's sake!"
        elif lt > 0 and le == 0:
            msg = "For fuck's sake, {0}!".format(target)
        else:
            msg = "For fuck's sake, {0}!  {1}".format(target, extra)
        print(msg)

    def field(self):
        if lt == 0 and le == 0 and ls == 0:
            msg = "And I said unto thee, 'Verily, cast thine eyes upon the field in which I grow my fucks,' and thou gave witness unto the field and saw that it was barren."
        elif lt > 0 and le == 0 and ls == 0:
            msg = "And I said unto {0}, 'Verily, cast thine eyes upon the field in which I grow my fucks,' and {1} gave witness unto the field and saw that it was barren.".format(target, target)
        if lt == 0 and le == 0 and ls > 0:
            msg = "And {0} said unto thee, 'Verily, cast thine eyes upon the field in which I grow my fucks,' and thou gave witness unto the field and saw that it was barren.".format(sender)
        elif lt == 0 and le > 0 and ls > 0:
            msg = "And {0} said unto thee, 'Verily, cast thine eyes upon the field in which I grow my fucks,' and thou gave witness unto the field and saw that it was barren.  {1}".format(sender, extra)
        elif lt > 0 and ls > 0 and le == 0:
            msg = "And {0} said unto {1}, 'Verily, cast thine eyes upon the field in which I grow my fucks,' and {2} gave witness unto the field and saw that it was barren.".format(sender, target, target)
        elif lt > 0 and ls > 0 and le > 0:
            msg = "And {0} said unto {1}, 'Verily, cast thine eyes upon the field in which I grow my fucks,' and {2} gave witness unto the field and saw that it was barren.  {3}".format(sender, target, target, extra)
        print(msg)

    def figjam(self):
        if lt == 0:
            msg = "Fuck I'm good, just ask me!"
        else:
            msg = "Fuck I'm good, {0}, just ask me!".format(target)
        print(msg)

    def fire(self):
        if lt == 0:
            msg = "Die in a fire."
        else:
            msg = "{0}, just fucking die in a fire.".format(target)
        print(msg)

    def flying(self):
        if lt == 0:
            msg = "I don't give a flying fuck!"
        else:
            msg = "{0}, I really don't give a flying fuck!".format(target)
        print(msg)

    def foad(self):
        if "foad" in sa[0]:
            exec("fuck().foad1()")
        else:
            print("Help guide for foad.py (pydoc3 foad).")

    def foad1(self):
        if lt == 0:
            msg = "Fuck off and die!"
        elif lt > 0 and le == 0:
            msg = "{0}, fuck off and die!".format(target)
        else:
            msg = "{0}, fuck off and die!  {1}".format(target, extra)
        print(msg)

    def froad(self):
        if lt == 0:
            msg = "Fuck right off and die!"
        elif lt > 0 and le == 0:
            msg = "{0}, fuck right off and die!".format(target)
        else:
            msg = "{0}, fuck right off and die!  {1}".format(target, extra)
        print(msg)

    def fubar(self):
        if lt == 0:
            msg = "Fucked Up Beyond All Recognition."
        else:
            msg = "{0}, fucked up beyond all recognition.".format(target)
        print(msg)

    def fubaru(self):
        if lt == 0:
            msg = "You're fucked up beyond all recognition."
        else:
            msg = "{0}, you're fucked up beyond all recognition.".format(target)
        print(msg)

    def fucker(self):
        if lt == 0:
            msg = "Fuck that fucking fucker!"
        else:
            msg = "Fuck {0}, that fucking fucker!".format(target)
        print(msg)

    def fuckers(self):
        if lt == 0:
            msg = "Fuck the fucking fuckers!"
        else:
            msg = "Fuck {0}, those fucking fuckers!".format(target)
        print(msg)

    def fuckety(self):
        msg = "Fuckety, fuck, fuck, fuck!"
        print(msg)

    def get(self):
        if lt == 0:
            msg = "Get fucked!"
        else:
            msg = "Get fucked {0}!".format(target)
        print(msg)

    def give(self):
        if lt == 0:
            msg = "I don't give a fuck."
        else:
            msg = "{0}, I really don't give a fuck.".format(target)
        print(msg)

    def gived(self):
        if lt == 0:
            msg = "I really don't give a fuck what they do."
        else:
            msg = "{0}, I really don't give a fuck what you do.".format(target)
        print(msg)

    def gives(self):
        if lt == 0:
            msg = "I really don't give a fuck what they say."
        else:
            msg = "{0}, I really don't give a fuck what you say.".format(target)
        print(msg)

    def givet(self):
        if lt == 0:
            msg = "I really don't give a fuck what they think."
        else:
            msg = "{0}, I really don't give a fuck what you think.".format(target)
        print(msg)

    def givew(self):
        if lt == 0:
            msg = "I really don't give a fuck who they are."
        else:
            msg = "{0}, I really don't give a fuck who you are.".format(target)
        print(msg)

    def go(self):
        if lt == 0:
            msg = "Go fuck yourself."
        else:
            msg = "{0}, go fuck yourself.".format(target)
        print(msg)

    def goget(self):
        if lt == 0:
            msg = "Go and get fucked!"
        else:
            msg = "Go and get fucked {0}!".format(target)
        print(msg)

    def gtfo1(self):
        if lt == 0:
            msg = "Get the fuck out!"
        else:
            msg = "{0}, get the fuck out!".format(target)
        print(msg)

    def gtfo2(self):
        if lt == 0:
            msg = "Let's get the fuck out of here!"
        else:
            msg = "{0}, let's get the fuck out of here!".format(target)
        print(msg)

    def hell(self):
        if lt == 0:
            msg = "Fucking Hell!"
        else:
            msg = "Fucking Hell, {0}!".format(target)
        print(msg)

    def hellf(self):
        if lt == 0:
            msg = "Hell will freeze before that happens."
        else:
            msg = "{0}, Hell will freeze before that happens.".format(target)
        print(msg)

    def hellfif(self):
        if lt == 0:
            msg = "Hell will freeze before I fuck you."
        else:
            msg = "{0}, Hell will freeze before I fuck you.".format(target)
        print(msg)

    def heygo(self):
        if lt == 0:
            msg = "Go and fuck yourself!"
        else:
            msg = "Hey {0}, go fuck yourself!".format(target)
        print(msg)

    def holy(self):
        if lt == 0:
            msg = "Holy fucking shit!"
        else:
            msg = "Holy fucking shit, {0}!".format(target)
        print(msg)

    def how1(self):
        if lt == 0:
            msg = "How the fuck did that happen?"
        else:
            msg = "{0}, how the fuck did that happen?".format(target)
        print(msg)

    def how2(self):
        if lt == 0:
            msg = "How the fuck does that work?"
        else:
            msg = "{0}, how the fuck does that work?".format(target)
        print(msg)

    def htfu(self):
        if lt == 0:
            msg = "Harden the fuck up!"
        else:
            msg = "{0}, harden the fuck up!".format(target)
        print(msg)

    def it(self):
        if lt == 0:
            msg = "Fuck it."
        else:
            msg = "{0}, fuck it.".format(target)
        print(msg)

    def incred(self):
        if lt == 0:
            msg = "In-fucking-credible!"
        else:
            msg = "In-fucking-credible {0}!".format(target)
        print(msg)

    def jams(self):
        msg = "Kick out the Jams, motherfucker!"
        print(msg)

    def jesus(self):
        msg = "Jesus Fucking Christ!"
        print(msg)

    def jfgi(self):
        if lt == 0:
            msg = "Just fucking Google it."
        else:
            msg = "{0}, just fucking Google it.".format(target)
        print(msg)

    def kidding(self):
        if lt == 0:
            msg = "Are you fucking kidding me?"
        else:
            msg = "{0}, are you fucking kidding me?".format(target)
        print(msg)

    def king(self):
        if lt == 0:
            msg = "Oh fuck off, just really fuck off you total dickface.  Christ you are fucking thick!"
        else:
            msg = "Oh fuck off, just really fuck off you total dickface.  Christ {0}, you are fucking thick!".format(target)
        print(msg)

    def kirsan(self):
        if lt == 0 and le == 0:
            msg = "You are as corrupt, delusional, megalomaniacal, vindictive and just as fucking crazy as that fucktard Kirsan Ilyumzhinov!"
        elif lt > 0 and le == 0:
            msg = "{0}, you are as corrupt, delusional, megalomaniacal, vindictive and just as fucking crazy as that fucktard Kirsan Ilyumzhinov!".format(target)
        else:
            msg = "{0}, you are as corrupt, delusional, megalomaniacal, vindictive and just as fucking crazy as that fucktard Kirsan Ilyumzhinov!  {1}".format(target, extra)
        print(msg)

    def know(self):
        if lt == 0:
            msg = "Fucked if I know!"
        else:
            msg = "{0}, fucked if I know!".format(target)
        print(msg)

    def liar(self):
        if lt == 0:
            msg = "You're a lying sack of shit!"
        else:
            msg = "{0}, you're a lying sack of shit!".format(target)
        print(msg)

    def liarf(self):
        if lt == 0:
            msg = "You're such a fucking liar, just so full of shit!"
        else:
            msg = "You're such a fucking liar, {0}, just so full of shit!".format(target)
        print(msg)

    def life(self):
        msg = "Fuck my life!"
        print(msg)

    def linus(self):
        if lt == 0:
            msg = "There aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap."
        else:
            msg = "{0}, there aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap.".format(target)
        print(msg)

    def lmfao(self):
        if lt == 0:
            msg = "Laughing my fucking arse off."
        else:
            msg = "{0}, laughing my fucking arse off.".format(target)
        print(msg)

    def madison(self):
        if lt == 0:
            msg = "What you've just said is one of the most insanely idiotic things I have ever heard.  At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought.  Everyone in this room is now dumber for having listened to it.  I award you no points."
        else:
            msg = "What you've just said is one of the most insanely idiotic things I have ever heard, {0}.  At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought.  Everyone in this room is now dumber for having listened to it.  I award you no points {1}, and may God have mercy on your soul because no one here will.".format(target, target)
        print(msg)

    def me(self):
        msg = "Fuck me!"
        print(msg)

    def mental(self):
        if lt == 0:
            msg = "You are fucking mental!"
        else:
            msg = "{0}, you are fucking mental!".format(target)
        print(msg)

    def mind(self):
        if lt == 0:
            msg = "Are you out of your fucking mind?!"
        else:
            msg = "{0}, are you out of your fucking mind?!".format(target)
        print(msg)

    def mofo(self):
        if lt == 0:
            msg = "Motherfucker!"
        else:
            msg = "{0}, you motherfucker!".format(target)
        print(msg)

    def mofos(self):
        if lt == 0:
            msg = "Motherfuckers!"
        else:
            msg = "{0}, you motherfuckers!".format(target)
        print(msg)

    def money1(self):
        if lt == 0:
            msg = "Show me the fucking money?!"
        else:
            msg = "{0}, show me the fucking money?!".format(target)
        print(msg)

    def money2(self):
        if lt == 0:
            msg = "Where's my fucking money?!"
        else:
            msg = "{0}, where's my fucking money?!".format(target)
        print(msg)

    def nfcd(self):
        if lt == 0:
            msg = "Not fucking cool, dude."
        else:
            msg = "Not fucking cool, {0}.".format(target)
        print(msg)

    def nfi1(self):
        if lt == 0:
            msg = "No fucking idea!"
        else:
            msg = "{0}, do you have any fucking idea?".format(target)
        print(msg)

    def nfi2(self):
        if lt == 0:
            msg = "I've got no fucking idea!"
        else:
            msg = "{0}, I've got no fucking idea!".format(target)
        print(msg)

    def nfi3(self):
        if lt == 0:
            msg = "You've got no fucking idea!"
        else:
            msg = "{0}, you've clearly got no fucking idea!".format(target)
        print(msg)

    def nmfp1(self):
        if lt == 0:
            msg = "It's not my fucking problem."
        else:
            msg = "{0}, it's not my fucking problem.".format(target)
        print(msg)

    def nmfp2(self):
        if lt == 0:
            msg = "That's not my fucking problem."
        else:
            msg = "{0}, that's not my fucking problem.".format(target)
        print(msg)

    def nonbiz(self):
        if lt == 0:
            msg = "That's none of your fucking business."
        else:
            msg = "{0}, that's none of your fucking business.".format(target)
        print(msg)

    def noreally(self):
        if lt == 0:
            msg = "Fuck you. No really, I mean it, go fuck yourselves."
        else:
            msg = "Fuck you {0}. No really, I mean it most sincerely, please go and fuck yourselves.".format(target)
            print(msg)

    def noshit(self):
        if lt == 0:
            msg = "No shit!"
        else:
            msg = "{0}, no shit!".format(target)
        print(msg)

    def noshitf(self):
        if lt == 0:
            msg = "No fucking shit!"
        else:
            msg = "{0}, no fucking shit!".format(target)
        print(msg)

    def noshitfq(self):
        if lt == 0:
            msg = "No fucking shit?!"
        else:
            msg = "{0}, no fucking shit?!".format(target)
        print(msg)

    def noshitq(self):
        if lt == 0:
            msg = "No shit?"
        else:
            msg = "{0}, no shit?".format(target)
        print(msg)

    def noway(self):
        if lt == 0:
            msg = "No fucking way!"
        else:
            msg = "{0}, there's no fucking way!".format(target)
        print(msg)

    def nsfch(self):
        if lt == 0:
            msg = "Not a snowflake's fucking chance in Hell!"
        else:
            msg = "{0}, there's not a snowflake's fucking chance in Hell!".format(target)
        print(msg)

    def nsfcht(self):
        if lt == 0:
            msg = "There's not a snowflake's fucking chance in Hell of that!"
        else:
            msg = "{0}, there's not a snowflake's fucking chance in Hell of that!".format(target)
        print(msg)

    def nsfh(self):
        if lt == 0:
            msg = "Not a snowflake's chance in Hell!"
        else:
            msg = "{0}, there's not a snowflake's chance in Hell!".format(target)
        print(msg)

    def nsfw(self):
        if lt == 0:
            msg = "Not safe for work?  Of course it's not fucking safe for work!"
        else:
            msg = "Not safe for work?  {0}, of course it's not fucking safe for work!".format(target)
        print(msg)

    def nugget(self):
        if lt == 0 and ls == 0 and le == 0:
            msg = "Well, aren't you a shining example of a rancid fuck-nugget."
        elif lt > 0 and ls == 0 and le == 0:
            msg = "Well {0}, aren't you a shining example of a rancid fuck-nugget.".format(target)
        elif lt > 0 and ls > 0 and le == 0:
            msg = "Well {0}, aren't you a shining example of a rancid fuck-nugget.  -- {1}".format(target, sender)
        elif lt > 0 and ls == 0 and le > 0:
            msg = "Well {0}, aren't you a shining example of a rancid fuck-nugget.  {1}".format(target, extra)
        else:
            msg = "Well {0}, aren't you a shining example of a rancid fuck-nugget.  {1}  -- {2}".format(target, extra, sender)
        print(msg)

    def oath1(self):
        if lt == 0:
            msg = "Fuck oath!"
        else:
            msg = "{0}, fuck oath!".format(target)
        print(msg)

    def oath2(self):
        if lt == 0:
            msg = "Fucking oath!"
        else:
            msg = "{0}, fucking oath!".format(target)
        print(msg)

    def oath3(self):
        if lt == 0:
            msg = "Fuckin' oath!"
        else:
            msg = "{0}, fuckin' oath!".format(target)
        print(msg)

    def off(self):
        if lt == 0:
            msg = "Fuck off!"
        else:
            msg = "Fuck off {0}!".format(target)
        print(msg)

    def omnia(self):
        if lt == 0:
            msg = "Omnia quia sunt, futūtum sunt."
            # All things that are, are fucked.
        else:
            msg = "{0}, omnia quia sunt, futūtum sunt.".format(target)
        print(msg)

    def outside(self):
        if lt == 0:
            msg = "Why don't you go outside and play hide-and-go-fuck-yourself?"
        else:
            msg = "{0}, why don't you go outside and play hide-and-go-fuck-yourself?".format(target)
        print(msg)

    def pink(self):
        msg = "Well, fuck me pink!"
        print(msg)

    def ppdata(self):
        if lt == 0 and le == 0:
            msg = "What the fuck kind of variable name is \"data\"?!  You should be incarcerated."
        elif lt > 0 and le == 0:
            msg = "What the fuck kind of variable name is \"data\"?!  You should be incarcerated, {0}.".format(target)
        elif lt > 0 and le > 0:
            msg = "What the fuck kind of variable name is \"{0}\"?!  You should be incarcerated, {1}.".format(extra, target)
        elif lt == 0 and le == 0 and len(cite) > 0:
            msg = "What the fuck kind of variable name is \"data\"?!  You should be incarcerated.  http://theprofoundprogrammer.com/post/25728479232/text-what-the-fuck-kind-of-variable-name-is".format(extra, target)
        elif lt > 0 and le == 0 and len(cite) > 0:
            msg = "What the fuck kind of variable name is \"data\"?!  You should be incarcerated, {1}.  http://theprofoundprogrammer.com/post/25728479232/text-what-the-fuck-kind-of-variable-name-is".format(extra, target)
        elif lt > 0 and le > 0 and len(cite) > 0:
            msg = "What the fuck kind of variable name is \"{0}\"?!  You should be incarcerated, {1}.  http://theprofoundprogrammer.com/post/25728479232/text-what-the-fuck-kind-of-variable-name-is".format(extra, target)
        print(msg)

    def ppwrote(self):
        if lt == 0:
            msg = "There's no fucking way I wrote this.  This is awful ... what the fuck does this even do?!"
        elif lt > 0:
            msg = "There's no fucking way I wrote this, {0}.  This is awful ... what the fuck does this even do?!".format(target)
        elif lt == 0 and cite is True:
            msg = "There's no fucking way I wrote this.  This is awful ... what the fuck does this even do?!  http://theprofoundprogrammer.com/post/25728609992/text-theres-no-fucking-way-i-wrote-this-this"
        elif lt > 0 and cite is True:
            msg = "There's no fucking way I wrote this, {0}.  This is awful ... what the fuck does this even do?!  http://theprofoundprogrammer.com/post/25728609992/text-theres-no-fucking-way-i-wrote-this-this".format(target)
        print(msg)

    def priapus(self):
        if lt == 0:
            msg = "Obscenis, peream, Priape, si non uti me pudet improbisque verbis sed cum tu posito deus pudore ostendas mihi coleos patentes cum cunno mihi mentula est vocanda."
        else:
            msg = "Obscenis, peream, {0}, si non uti me pudet improbisque verbis sed cum tu posito degenerem pudore ostendas mihi coleos patentes cum cunno mihi mentula est vocanda.".format(target)
        print(msg)

    def priapus_trans1(self):
        if lt == 0:
            msg = "I'd rather die than use obscene and improper words; but when you, as a degenerate, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks."
        else:
            msg = "I'd rather die than use obscene and improper words; but when you, {0}, as a degenerate, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks.".format(target)
        print(msg)

    def priapus_trans2(self):
        if lt == 0:
            msg = "I'd rather die than use obscene and improper words; but when you, Priapus, as a god, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks."
        else:
            msg = "I'd rather die than use obscene and improper words; but when you, {0}, as an inferior, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks.".format(target)
        print(msg)

    def psycho1(self):
        if lt == 0:
            msg = "You fucking megalomaniacal, malignantly narcissistic, psychopath!"
        else:
            msg = "{0}, you fucking megalomaniacal, malignantly narcissistic, psychopath!".format(target)
        print(msg)

    def psycho2(self):
        if lt == 0:
            msg = "You fucking megalomaniacal, malignantly narcissistic, sociopath!"
        else:
            msg = "{0}, you fucking megalomaniacal, malignantly narcissistic, sociopath!".format(target)
        print(msg)

    def psycho3(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, psychopath!"
        else:
            msg = "{0}, you're a fucking megalomaniacal, malignantly narcissistic, psychopath!".format(target)
        print(msg)

    def psycho4(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, sociopath!"
        else:
            msg = "{0}, you're a fucking megalomaniacal, malignantly narcissistic, sociopath!".format(target)
        print(msg)

    def psycho5(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, psychopathic cunt!"
        else:
            msg = "{0}, you're a fucking megalomaniacal, malignantly narcissistic, psychopathic cunt!".format(target)
        print(msg)

    def psycho6(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, sociopathic cunt!"
        else:
            msg = "{0}, you're a fucking megalomaniacal, malignantly narcissistic, sociopathic cunt!".format(target)
        print(msg)

    def ratm(self):
        if lt == 0:
            msg = "Fuck you! I won't do what you tell me!"
        else:
            msg = "Fuck you {0}! I won't do what you tell me!".format(target)
        print(msg)

    def roff(self):
        if lt == 0:
            msg = "You can fuck right off!"
        else:
            msg = "{0}, you can fuck right off!".format(target)
        print(msg)

    def royal(self):
        if lt == 0:
            msg = "It's right royally fucked!"
        else:
            msg = "{0}, it's right royally fucked!".format(target)
        print(msg)

    def royalwe(self):
        if lt == 0:
            msg = "We're right royally fucked!"
        else:
            msg = "{0}, we're right royally fucked!".format(target)
        print(msg)

    def rtfm(self):
        if lt == 0:
            msg = "Read the fucking manual!"
        else:
            msg = "{0}, read the fucking manual!".format(target)
        print(msg)

    def sb1(self):
        if lt == 0:
            msg = "You fucking son of a bitch!"
        else:
            msg = "{0}, you fucking son of a bitch!".format(target)
        print(msg)

    def sb2(self):
        if lt == 0:
            msg = "You're a fucking son of a bitch!"
        else:
            msg = "{0}, you're a fucking son of a bitch!".format(target)
        print(msg)

    def script(self):
        if lt == 0:
            msg = "Is this a script?  Of course it's a fucking script?!"
        else:
            msg = "Is this a script?  Yes {0}, of course it's a fucking script?!".format(target)
        print(msg)

    def sfa(self):
        if lt == 0:
            msg = "Sweet fuck all."
        else:
            msg = "{0}, sweet fuck all.".format(target)
        print(msg)

    def sfac(self):
        if lt == 0:
            msg = "The chances of that are about three fifths of sweet fuck all."
        else:
            msg = "{0}, the chances of that are about three fifths of sweet fuck all.".format(target)
        print(msg)

    def shakespeare(self):
        if lt == 0:
            msg = "Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch!"
        else:
            msg = "{0}, thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch!".format(target)
        print(msg)

    def sherlock(self):
        if lt == 0:
            msg = "No shit, Sherlock!"
        else:
            msg = "{0}, no shit, Sherlock!".format(target)
        print(msg)

    def shit(self):
        if lt == 0:
            msg = "Fuck this shit!"
        else:
            msg = "{0}, fuck your shit!".format(target)
        print(msg)

    def sideways(self):
        msg = "Well, fuck me sideways!"
        print(msg)

    def snafu(self):
        if lt == 0:
            msg = "Situation Normal: All Fucked Up!"
        else:
            msg = "{0}, it's situation normal: all fucked up!".format(target)
        print(msg)

    def stfu(self):
        if lt == 0:
            msg = "Shut the fuck up!"
        else:
            msg = "{0}, shut the fuck up!".format(target)
        print(msg)

    def stigmata(self):
        if lt == 0:
            msg = "Fuck the Church!  Fuck the State!  Fuck you!  Fuck me!  Fuck all these arseholes!"
        else:
            msg = "Fuck {0}!  Fuck the Church!  Fuck the State!  Fuck you!  Fuck me!  Fuck all these arseholes!".format(target)
        print(msg)

    def stolen(self):
        if lt == 0:
            msg = "I wouldn't fuck you with a stolen dick!"
        else:
            msg = "I wouldn't fuck {0} with a stolen dick!".format(target)
        print(msg)

    def suns(self):
        if lt == 0 and ls == 0 and le == 0:
            msg = "Fuck you with the fury of a thousand suns."
        elif lt > 0 and ls == 0 and le == 0:
            msg = "{0}, fuck you with the fury of a thousand suns.".format(target)
        elif lt > 0 and ls > 0 and le == 0:
            msg = "{0}, fuck you with the fury of a thousand suns.  -- {1}".format(target, sender)
        elif lt > 0 and ls == 0 and le > 0:
            msg = "{0}, fuck you with the fury of a thousand suns.  {1}".format(target, extra)
        else:
            msg = "{0}, fuck you with the fury of a thousand suns.  {1} -- {2}".format(target, extra, sender)
        print(msg)

    def survey(self):
        if lt == 0:
            msg = "Hmm, survey says ... go fuck yourself!"
        else:
            msg = "{0}, survey says ... go fuck yourself!".format(target)
        print(msg)

    def tard(self):
        if lt == 0:
            msg = "You complete and utter fucktard!"
        else:
            msg = "{0}, you are a complete and utter fucktard!".format(target)
        print(msg)

    def tfwo(self):
        if lt == 0:
            msg = "I'm totally fucking weirded out by that."
        else:
            msg = "{0}, you're totally fucking weirding me out.".format(target)
        print(msg)

    def thanks(self):
        if lt == 0:
            msg = "Fuck you very much."
        else:
            msg = "Fuck you very much, {0}.".format(target)
        print(msg)

    def tism(self):
        if lt == 0:
            msg = "I might be a cunt, but I'm not a fucking cunt."
        else:
            msg = "I might be a cunt, {0}, but I'm not a fucking cunt.".format(target)
        print(msg)

    def totgaf(self):
        if lt == 0:
            msg = "I'm too old to give a fuck."
        else:
            msg = "{0}, I'm too old to give a fuck.".format(target)
        print(msg)

    def ucunt(self):
        if lt == 0:
            msg = "You cunt!"
        else:
            msg = "{0}, you cunt!".format(target)
        print(msg)

    def up1(self):
        if lt == 0:
            msg = "I'm gonna fuck you up!"
        else:
            msg = "{0}, I'm gonna fuck you up!".format(target)
        print(msg)

    def up2(self):
        if lt == 0:
            msg = "I'm all fucked up!"
        else:
            msg = "{0}, I'm all fucked up!".format(target)
        print(msg)

    def up3(self):
        if lt == 0:
            msg = "I'm completely fucked up!"
        else:
            msg = "{0}, I'm completely fucked up!".format(target)
        print(msg)

    def urcunt(self):
        if lt == 0:
            msg = "You're a cunt!"
        else:
            msg = "{0}, you're a cunt!".format(target)
        print(msg)

    def urfcunt(self):
        if lt == 0:
            msg = "You're a fucking cunt!"
        else:
            msg = "{0}, you're a fucking cunt!".format(target)
        print(msg)

    def urso1(self):
        if lt == 0:
            msg = "You are so fucked."
        else:
            msg = "You are so fucked, {0}.".format(target)
        print(msg)

    def urso2(self):
        if lt == 0:
            msg = "You are so fucked, so fucking fucked!"
        else:
            msg = "You are so fucked, {0}, so fucking fucked!".format(target)
        print(msg)

    def utard(self):
        if lt == 0:
            msg = "You fucktard!"
        else:
            msg = "{0}, you fucktard!".format(target)
        print(msg)

    def valley(self):
        if lt == 0:
            msg = "Yea, though I walk through the shadow of the Valley of Death I shall fear no evil ... for I am the meanest motherfucker in all the land!"
        else:
            msg = "Yea, {0}, though I walk through the shadow of the Valley of Death I shall fear no evil ... for I am the meanest motherfucker in all the land!".format(target)
        print(msg)

    def vvv(self):
        msg = "Vidi, vici, veni."  # "I saw, I conquered, I came"
        print(msg)

    def wafwot(self):
        if lt == 0:
            msg = "What a fucking waste of time!"
        else:
            msg = "{0}, that's a fucking waste of time!".format(target)
        print(msg)

    def wbfu(self):
        if lt == 0:
            msg = "Why?  Because fuck you, that's why."
        else:
            msg = "Why?  Because fuck you {0}, that's why.".format(target)
        print(msg)

    def when1(self):
        if lt == 0:
            msg = "When the fuck will that happen?"
        else:
            msg = "{0}, when the fuck will that happen?".format(target)
        print(msg)

    def when2(self):
        if lt == 0:
            msg = "When the fuck will we get there?"
        else:
            msg = "{0}, when the fuck will we get there?".format(target)
        print(msg)

    def where1(self):
        if lt == 0:
            msg = "Where the fuck are we?"
        else:
            msg = "{0}, where the fuck are we?".format(target)
        print(msg)

    def where2(self):
        if lt == 0:
            msg = "Where the fuck is it?"
        else:
            msg = "{0}, where the fuck is it?".format(target)
        print(msg)

    def who1(self):
        if lt == 0:
            msg = "Who the fuck do they think they are?"
        else:
            msg = "{0}, who the fuck do they think they are?".format(target)
        print(msg)

    def who2(self):
        if lt == 0:
            msg = "Who the fuck do they think you are?"
        else:
            msg = "{0}, who the fuck do they think you are?".format(target)
        print(msg)

    def who3(self):
        if lt == 0:
            msg = "Who the fuck do you think you are?"
        else:
            msg = "{0}, who the fuck do you think you are?".format(target)
        print(msg)

    def who3(self):
        if lt == 0:
            msg = "Who the fuck knows?"
        else:
            msg = "{0}, who the fuck knows?".format(target)
        print(msg)

    def why(self):
        if lt == 0:
            msg = "Why the fuck should I?"
        else:
            msg = "{0}, why the fuck should I?".format(target)
        print(msg)

    def wit(self):
        if lt == 0:
            msg = "You fuckwit!"
        else:
            msg = "{0}, you fuckwit!".format(target)
        print(msg)

    def woftam(self):
        if lt == 0:
            msg = "It's a waste of fucking time and money."
        else:
            msg = "{0}, it's a waste of fucking time and money.".format(target)
        print(msg)

    def wtaf(self):
        if lt == 0:
            msg = "What the actual fuck?!"
        elif lt > 0:
            msg = "What the actual fuck {0}?!".format(target)
        else:
            msg = "What the actual fuck {0}?!  {1}".format(target, extra)
        print(msg)

    def wtf(self):
        if lt == 0:
            msg = "What the fuck?!"
        else:
            msg = "{0}, what the fuck?!".format(target)
        print(msg)

    def wtfc(self):
        if lt == 0:
            msg = "What fucking crack are you smoking?!"
        else:
            msg = "{0}, what fucking crack are you smoking?!".format(target)
        print(msg)

    def wtfd(self):
        if lt == 0:
            msg = "What the fuck are you doing?!"
        else:
            msg = "{0}, what the fuck are you doing?!".format(target)
        print(msg)

    def wtfg(self):
        if lt == 0:
            msg = "What the fuck is going on?!"
        else:
            msg = "{0}, what the fuck is going on?!".format(target)
        print(msg)

    def wtfgh(self):
        if lt == 0:
            msg = "What the fuck is going on here?!"
        else:
            msg = "{0}, what the fuck is going on here?!".format(target)
        print(msg)

    def wtfo(self):
        if lt == 0:
            msg = "What the fuck are you on?!"
        else:
            msg = "{0}, what the fuck are you on?!".format(target)
        print(msg)

    def wtft(self):
        if lt == 0:
            msg = "What the fuck is that?"
        else:
            msg = "{0}, what the fuck is that?".format(target)
        print(msg)

    def wtfta(self):
        if lt == 0:
            msg = "What the fuck are you talking about?!"
        else:
            msg = "{0}, what the fuck are you talking about?!".format(target)
        print(msg)

    def wtfu(self):
        if lt == 0:
            msg = "What the unutterable fuck?!"
        else:
            msg = "{0}, what the unutterable fuck?!".format(target)
        print(msg)

    def wtfwjd(self):
        if lt == 0:
            msg = "What the fuck would Jesus do?"
        else:
            msg = "{0}, so what the fuck would Jesus do?".format(target)
        print(msg)

    def wtfwjdrtfm(self):
        if lt == 0:
            msg = "What the fuck would Jesus do?  Jesus would read the fucking manual!"
        else:
            msg = "{0}, so what the fuck would Jesus do?  Jesus would read the fucking manual!".format(target)
        print(msg)

    def you(self):
        if lt == 0:
            msg = "Fuck you!"
        else:
            msg = "Fuck you {0}!".format(target)
        print(msg)


df0 = dir(fuck)
df = []
for x in df0:
    if "__" not in x:
        df.append(x)
del(df0)
del(x)
df.remove("foad1")
lc = len(df)

rf = []
for x in df:
    rf.append(x)
rf.remove("about")
rf.remove("acronym")
lr = len(rf)

random.seed()
rc = random.choice(rf)

if l < 2:
    print(about)
    print("")
    print("Number of defined options:  {0}".format(lc))
    print("")
elif l == 2 and wtf == "list_options":
    print("")
    print("{0}  {1}".format(__title__, __version__))
    print(__copyright__)
    print("")
    print("Number of defined options:  {0}".format(lc))
    print("")
    print(textwrap.fill("List of defined options:  " + ", ".join(df), 72))
    print("")
    print("Bitcoin:  {0}".format(__bitcoin__))
    print("")
elif l >= 3 and wtf == "sherlock" and target.lower()[0:8] == "sherlock":
    print("No shit, Sherlock!")
elif l >= 3 and wtf == "random" and rc == "sherlock" and target.lower()[0:8] == "sherlock":
    print("No shit, Sherlock!")
elif l == 2 and wtf == "unittest":
    print(about)
    print("")
    for i in range(lc):
        print("Command:  {0} -f {1} [-n {2} -e {3} -s {4}]".format(sa[0], df[i], "<target>", "<extra>", "<sender>"))
        try:
            exec("fuck().{0}()".format(df[i]))
        except(AttributeError, NameError):
            print("Fuck testing!")
        print("")
elif l >= 3 and wtf == "unittest":
    if target.lower() == "atitle":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "copyright":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "website":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "adversary":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "domain":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "donations":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "bitcoin":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "author":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "contact":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "email":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "encryption":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "gpg key":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "options":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "pirate":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "twitter":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "twython tools":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "version":
        print("Command:  {0} -f about -n {1}".format(sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "carnal":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "bond":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "die":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "right":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "title":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "cunt":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "foaas":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "snag":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "snafu":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "fubar":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "lmfao":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "figjam":
        print("Command:  {0} -f acronym -n {1}".format(sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    else:
        print(about)
        print("")
        for i in range(lc):
            if lt == 0 and le == 0 and ls == 0:
                print("Command:  {0} -f {1}".format(sa[0], df[i]))
                try:
                    exec("fuck().{0}()".format(df[i]))
                except(AttributeError, NameError):
                    print("Fuck testing!")
                print("")
            elif lt > 0 and le == 0 and ls == 0:
                print("Command:  {0} -f {1} -n \"{2}\"".format(sa[0], df[i], target))
                try:
                    exec("fuck().{0}()".format(df[i]))
                except(AttributeError, NameError):
                    print("Fuck testing!")
                print("")
            elif lt > 0 and le > 0 and ls == 0:
                print("Command:  {0} -f {1} -n \"{2}\" -e \"{3}\"".format(sa[0], df[i], target, extra))
                try:
                    exec("fuck().{0}()".format(df[i]))
                except(AttributeError, NameError):
                    print("Fuck testing!")
                print("")
            elif lt > 0 and le == 0 and ls > 0:
                print("Command:  {0} -f {1} -n \"{2}\" -s \"{3}\"".format(sa[0], df[i], target, sender))
                try:
                    exec("fuck().{0}()".format(df[i]))
                except(AttributeError, NameError):
                    print("Fuck testing!")
                print("")
            elif lt > 0 and le > 0 and ls > 0:
                print("Command:  {0} -f {1} -n \"{2}\" -e \"{3}\" -s \"{4}\"".format(sa[0], df[i], target, extra, sender))
                try:
                    exec("fuck().{0}()".format(df[i]))
                except(AttributeError, NameError):
                    print("Fuck testing!")
                print("")
elif l >= 2 and wtf == "random":
    try:
        exec("fuck().{0}()".format(rc))
    except(AttributeError, NameError):
        print("Fuck randomness!")
elif la == 3:
    if args.fuck is not None and args.name is None:
        try:
            exec("fuck().{0}()".format(wtf))
        except(AttributeError, NameError):
            print("Fuck {0}!".format(wtf))
    elif args.fuck is None and args.name is not None:
        print("Fuck {0}!".format(target))
elif la == 4:
    if args.fuck is not None and args.name is None:
        try:
            exec("fuck().{0}()".format(wtf))
        except(AttributeError, NameError):
            w = []
            for i in range(la - 2):
                w.append(str(sys.argv[i + 2]))
            wtf = " ".join(w)
            print("Fuck {0}!".format(wtf))
    elif args.fuck is None and args.name is not None:
        t = []
        for i in range(la - 2):
            t.append(str(sys.argv[i + 2]))
        target = " ".join(t)
        print("Fuck {0}!".format(target))
    elif args.fuck is not None and args.name is not None:
        try:
            exec("fuck().{0}()".format(wtf))
        except(AttributeError, NameError):
            print("Fuck {0}!".format(wtf))
    else:
        pass
        # print("Fuck Perl!")
elif la >= 5:
    if args.fuck is not None and args.name is None:
        try:
            exec("fuck().{0}()".format(wtf))
        except(AttributeError, NameError):
            w = []
            for i in range(la - 2):
                w.append(str(sys.argv[i + 2]))
            wtf = " ".join(w)
            print("Fuck {0}!".format(wtf))
    elif args.fuck is None and args.name is not None:
        t = []
        for i in range(la - 2):
            t.append(str(sys.argv[i + 2]))
        target = " ".join(t)
        print("Fuck {0}!".format(target))
    elif args.fuck is not None and args.name is not None:
        try:
            exec("fuck().{0}()".format(wtf))
        except(AttributeError, NameError):
            w = []
            for i in range(la - 2):
                if str(sys.argv[i]).startswith("-") is False:
                    w.append(str(sys.argv[i + 2]))
            wtfx = " ".join(w)
            print("Fuck {0}!".format(wtfx))
