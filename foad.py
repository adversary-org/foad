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
# Version:  0.6.1.5
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
#
# The old method of calling the script will still work, but only for
# the argument types available at this point (i.e. --fuck and --name).
# Any future argument types (e.g. the planned --extra) will not be
# available through the old method.  When using this old method the
# order the options are specified is important.
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
__license__ = "GNU Public License version 3 (GPLv3)"
__version__ = "0.6.1.5"
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
%s
Version %s
%s
License:  %s

For instructions run:  %s -h

Contact:  %s %s
Bitcoin:  %s
""" % (__title__, __version__, __copyright__, __license__, sys.argv[0], __author__, __openpgp__, __bitcoin__)

version = "%s (foad.py) version %s" % (__stitle__, __version__)

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

        For more help run:  pydoc3 foad

        https://github.com/adversary-org/foad

        Bitcoin:  %s

    %s
    %s
    """ % (__bitcoin__, version, __copyright__)))
parser.add_argument("-f", "--fuck", help="One word, indicates type of fuck to give, run foad.py -f list_options to see possible flags.", action="store", required=False)
parser.add_argument("-n", "--name", help="Name of target, more than one word must be in quotation marks.", action="store", required=False)
# parser.add_argument("-e", "--extra", help="Additional comment to append to output", action="store", required=False)
# parser.add_argument("-v", "--version", help="Print the version number.", action=print(version), required=False)

if len(sys.argv) > lx:
    la = len(sys.argv)
else:
    la = lx

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

lt = len(target)


class fuck:
    def a(self):
        if lt == 0:
            msg = "Fuckin' A!"
        else:
            msg = "%s, fuckin' A!" % target
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
            msg = "Number of defined options:  %d" % (lc)
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
        else:
            msg = "Abso-fucking-lutely %s!" % target
        print(msg)

    def amaze(self):
        if lt == 0:
            msg = "That was fucking amazing!"
        else:
            msg = "%s, that was fucking amazing!" % target
        print(msg)

    def bbm(self):
        msg = "Big bad motherfucker."
        print(msg)

    def cango(self):
        if lt == 0:
            msg = "They can go and fuck themselves."
        else:
            msg = "%s can go and fuck themselves." % target
        print(msg)

    def cbf(self):
        if lt == 0:
            msg = "I can't be fucked!"
        else:
            msg = "%s, I can't be fucked!" % target
        print(msg)

    def chainsaw(self):
        if lt == 0:
            msg = "Fuck me gently with a chainsaw.  Do I look like Mother Teresa?"
        else:
            msg = "Fuck me gently with a chainsaw, %s.  Do I look like Mother Teresa?" % target
        print(msg)

    def chainsawe(self):
        if lt == 0:
            msg = "Fuck me gently with a chainsaw!  Do I look like Mother Teresa?!"
        else:
            msg = "Fuck me gently with a chainsaw, %s!  Do I look like Mother Teresa?!" % target
        print(msg)

    def chainsaws(self):
        if lt == 0:
            msg = "Fuck me gently with a chainsaw!"
        else:
            msg = "Fuck me gently with a chainsaw, %s!" % target
        print(msg)

    def cfm(self):
        if lt == 0:
            msg = "Come fuck me."
        else:
            msg = "%s, come fuck me." % target
        print(msg)

    def cluster(self):
        if lt == 0:
            msg = "It's a total cluster-fuck!"
        else:
            msg = "%s, it's a total cluster-fuck!" % target
        print(msg)

    def clustera(self):
        if lt == 0:
            msg = "It's an almighty cluster-fuck!"
        else:
            msg = "%s, it's an almighty cluster-fuck!" % target
        print(msg)

    def cocksuck(self):
        if lt == 0:
            msg = "Fuck you, you fucking cocksucker!"
        else:
            msg = "Fuck you %s, you fucking cocksucker!" % target
        print(msg)

    def compleat(self):
        if lt == 0:
            msg = "I might be a cunt, but I'm not a fucking cunt."
        else:
            msg = "I might be a cunt, %s, but I'm not a fucking cunt." % target
        print(msg)

    def cracked(self):
        if lt == 0:
            msg = "You are fucking cracked!"
        else:
            msg = "%s, you are fucking cracked!" % target
        print(msg)

    def cunt(self):
        if lt == 0:
            msg = "Fuck you, you complete and utter fucking cunt!"
        else:
            msg = "Fuck you %s, you complete and utter fucking cunt!" % target
        print(msg)

    def cunts(self):
        if lt == 0:
            msg = "Fuck you, you complete and utter fucking cunts!"
        else:
            msg = "Fuck you %s, you complete and utter fucking cunts!" % target
        print(msg)

    def cuntz(self):
        if lt == 0:
            msg = "Fuck all those complete and utter fucking cocksuckers and cunts!"
        else:
            msg = "Fuck the %s, they're all complete and utter fucking cocksuckers and cunts!" % target
        print(msg)

    def custode(self):
        if lt == 0:
            msg = "Sed quis custodiet ipsos futūtor?"
            # But who will guard the fucker(s)?
        else:
            msg = "%s, quis custodiet ipsos futūtor?" % target
        print(msg)

    def deadwood(self):
        if lt == 0:
            msg = "You fucking cocksucker!"
        else:
            msg = "%s, you're a fucking cocksucker!" % target
        print(msg)

    def denial(self):
        if lt == 0:
            msg = "I didn't fucking do it!"
        else:
            msg = "%s, I didn't fucking do it!" % target
        print(msg)

    def disbelief(self):
        if lt == 0:
            msg = "Un-fucking-believable!"
        else:
            msg = "Un-fucking-believable %s!" % target
        print(msg)

    def does(self):
        if lt == 0:
            msg = "Does it look like I give a fuck?"
        else:
            msg = "%s, does it look like I give a fuck?" % target
        print(msg)

    def donut(self):
        if lt == 0:
            msg = "Go and take a flying fuck at a rolling donut."
        else:
            msg = "%s, go and take a flying fuck at a rolling donut." % target
        print(msg)

    def doodle(self):
        msg = "Fuck-a-doodle-doo!"
        print(msg)

    def dorothy(self):
        if lt == 0:
            msg = "Too fucking busy and vice versa."  # Dorothy Parker
        else:
            msg = "%s, I'm too fucking busy and vice versa." % target
        print(msg)

    def duck(self):
        if lt == 0:
            msg = "Fuck a duck!"
        else:
            msg = "%s, fuck a duck!" % target
        print(msg)

    def english(self):
        if lt == 0:
            msg = "English motherfucker!  Do you speak it?!"
        else:
            msg = "English motherfucker!  Do you speak it %s?!" % target
        print(msg)

    def every1(self):
        if lt == 0:
            msg = "Everyone's fucked!"
        else:
            msg = "%s, everyone's fucked!" % target
        print(msg)

    def every2(self):
        if lt == 0:
            msg = "Everything's fucked!"
        else:
            msg = "%s, everything's fucked!" % target
        print(msg)

    def exorcist(self):
        if lt == 0:
            msg = "Your mother sucks cocks in Hell!"
        else:
            msg = "Your mother sucks cocks in Hell, %s!" % target
        print(msg)

    def fascinating(self):
        if lt == 0:
            msg = "Fascinating story, in what chapter do you shut the fuck up?"
        else:
            msg = "Fascinating story, %s, in what chapter do you shut the fuck up?" % target
        print(msg)

    def ffs(self):
        if lt == 0:
            msg = "For fuck's sake!"
        else:
            msg = "For fuck's sake, %s!" % target
        print(msg)

    def figjam(self):
        if lt == 0:
            msg = "Fuck I'm good, just ask me!"
        else:
            msg = "Fuck I'm good, %s, just ask me!" % target
        print(msg)

    def fire(self):
        if lt == 0:
            msg = "Die in a fire."
        else:
            msg = "%s, just fucking die in a fire." % target
        print(msg)

    def flying(self):
        if lt == 0:
            msg = "I don't give a flying fuck!"
        else:
            msg = "%s, I really don't give a flying fuck!" % target
        print(msg)

    def foad(self):
        if "foad" in sa[0]:
            exec("fuck().foad1()")
        else:
            print("Help guide for foad.py (pydoc3 foad).")

    def foad1(self):
        if lt == 0:
            msg = "Fuck off and die!"
        else:
            msg = "%s, fuck off and die!" % target
        print(msg)

    def froad(self):
        if lt == 0:
            msg = "Fuck right off and die!"
        else:
            msg = "%s, fuck right off and die!" % target
        print(msg)

    def fubar(self):
        if lt == 0:
            msg = "Fucked Up Beyond All Recognition."
        else:
            msg = "%s, fucked up beyond all recognition." % target
        print(msg)

    def fubaru(self):
        if lt == 0:
            msg = "You're fucked up beyond all recognition."
        else:
            msg = "%s, you're fucked up beyond all recognition." % target
        print(msg)

    def fucker(self):
        if lt == 0:
            msg = "Fuck that fucking fucker!"
        else:
            msg = "Fuck %s, that fucking fucker!" % target
        print(msg)

    def fuckers(self):
        if lt == 0:
            msg = "Fuck the fucking fuckers!"
        else:
            msg = "Fuck %s, those fucking fuckers!" % target
        print(msg)

    def fuckety(self):
        msg = "Fuckety, fuck, fuck, fuck!"
        print(msg)

    def get(self):
        if lt == 0:
            msg = "Get fucked!"
        else:
            msg = "Get fucked %s!" % target
        print(msg)

    def give(self):
        if lt == 0:
            msg = "I don't give a fuck."
        else:
            msg = "%s, I really don't give a fuck." % target
        print(msg)

    def gived(self):
        if lt == 0:
            msg = "I really don't give a fuck what they do."
        else:
            msg = "%s, I really don't give a fuck what you do." % target
        print(msg)

    def gives(self):
        if lt == 0:
            msg = "I really don't give a fuck what they say."
        else:
            msg = "%s, I really don't give a fuck what you say." % target
        print(msg)

    def givet(self):
        if lt == 0:
            msg = "I really don't give a fuck what they think."
        else:
            msg = "%s, I really don't give a fuck what you think." % target
        print(msg)

    def givew(self):
        if lt == 0:
            msg = "I really don't give a fuck who they are."
        else:
            msg = "%s, I really don't give a fuck who you are." % target
        print(msg)

    def go(self):
        if lt == 0:
            msg = "Go fuck yourself."
        else:
            msg = "%s, go fuck yourself." % target
        print(msg)

    def goget(self):
        if lt == 0:
            msg = "Go and get fucked!"
        else:
            msg = "Go and get fucked %s!" % target
        print(msg)

    def gtfo1(self):
        if lt == 0:
            msg = "Get the fuck out!"
        else:
            msg = "%s, get the fuck out!" % target
        print(msg)

    def gtfo2(self):
        if lt == 0:
            msg = "Let's get the fuck out of here!"
        else:
            msg = "%s, let's get the fuck out of here!" % target
        print(msg)

    def hell(self):
        if lt == 0:
            msg = "Fucking Hell!"
        else:
            msg = "Fucking Hell, %s!" % target
        print(msg)

    def hellf(self):
        if lt == 0:
            msg = "Hell will freeze before that happens."
        else:
            msg = "%s, Hell will freeze before that happens." % target
        print(msg)

    def hellfif(self):
        if lt == 0:
            msg = "Hell will freeze before I fuck you."
        else:
            msg = "%s, Hell will freeze before I fuck you." % target
        print(msg)

    def heygo(self):
        if lt == 0:
            msg = "Go and fuck yourself!"
        else:
            msg = "Hey %s, go fuck yourself!" % target
        print(msg)

    def holy(self):
        if lt == 0:
            msg = "Holy fucking shit!"
        else:
            msg = "Holy fucking shit, %s!" % target
        print(msg)

    def how1(self):
        if lt == 0:
            msg = "How the fuck did that happen?"
        else:
            msg = "%s, how the fuck did that happen?" % target
        print(msg)

    def how2(self):
        if lt == 0:
            msg = "How the fuck does that work?"
        else:
            msg = "%s, how the fuck does that work?" % target
        print(msg)

    def htfu(self):
        if lt == 0:
            msg = "Harden the fuck up!"
        else:
            msg = "%s, harden the fuck up!" % target
        print(msg)

    def it(self):
        if lt == 0:
            msg = "Fuck it."
        else:
            msg = "%s, fuck it." % target
        print(msg)

    def incred(self):
        if lt == 0:
            msg = "In-fucking-credible!"
        else:
            msg = "In-fucking-credible %s!" % target
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
            msg = "%s, just fucking Google it." % target
        print(msg)

    def kidding(self):
        if lt == 0:
            msg = "Are you fucking kidding me?"
        else:
            msg = "%s, are you fucking kidding me?" % target
        print(msg)

    def king(self):
        if lt == 0:
            msg = "Oh fuck off, just really fuck off you total dickface.  Christ you are fucking thick!"
        else:
            msg = "Oh fuck off, just really fuck off you total dickface.  Christ %s, you are fucking thick!" % target
        print(msg)

    def kirsan(self):
        if lt == 0:
            msg = "You are as corrupt, delusional, megalomaniacal, vindictive and just as fucking crazy as that fucktard Kirsan Ilyumzhinov!"
        else:
            msg = "%s, you are as corrupt, delusional, megalomaniacal, vindictive and just as fucking crazy as that fucktard Kirsan Ilyumzhinov!" % target
        print(msg)

    def know(self):
        if lt == 0:
            msg = "Fucked if I know!"
        else:
            msg = "%s, fucked if I know!" % target
        print(msg)

    def liar(self):
        if lt == 0:
            msg = "You're a lying sack of shit!"
        else:
            msg = "%s, you're a lying sack of shit!" % target
        print(msg)

    def liarf(self):
        if lt == 0:
            msg = "You're such a fucking liar, just so full of shit!"
        else:
            msg = "You're such a fucking liar, %s, just so full of shit!" % target
        print(msg)

    def life(self):
        msg = "Fuck my life!"
        print(msg)

    def linus(self):
        if lt == 0:
            msg = "There aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap."
        else:
            msg = "%s, there aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap." % target
        print(msg)

    def lmfao(self):
        if lt == 0:
            msg = "Laughing my fucking arse off."
        else:
            msg = "%s, laughing my fucking arse off." % target
        print(msg)

    def madison(self):
        if lt == 0:
            msg = "What you've just said is one of the most insanely idiotic things I have ever heard.  At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought.  Everyone in this room is now dumber for having listened to it.  I award you no points."
        else:
            msg = "What you've just said is one of the most insanely idiotic things I have ever heard, %s.  At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought.  Everyone in this room is now dumber for having listened to it.  I award you no points %s, and may God have mercy on your soul because no one here will." % (target, target)
        print(msg)

    def me(self):
        msg = "Fuck me!"
        print(msg)

    def mental(self):
        if lt == 0:
            msg = "You are fucking mental!"
        else:
            msg = "%s, you are fucking mental!" % target
        print(msg)

    def mind(self):
        if lt == 0:
            msg = "Are you out of your fucking mind?!"
        else:
            msg = "%s, are you out of your fucking mind?!" % target
        print(msg)

    def mofo(self):
        if lt == 0:
            msg = "Motherfucker!"
        else:
            msg = "%s, you motherfucker!" % target
        print(msg)

    def mofos(self):
        if lt == 0:
            msg = "Motherfuckers!"
        else:
            msg = "%s, you motherfuckers!" % target
        print(msg)

    def money1(self):
        if lt == 0:
            msg = "Show me the fucking money?!"
        else:
            msg = "%s, show me the fucking money?!" % target
        print(msg)

    def money2(self):
        if lt == 0:
            msg = "Where's my fucking money?!"
        else:
            msg = "%s, where's my fucking money?!" % target
        print(msg)

    def nfi1(self):
        if lt == 0:
            msg = "No fucking idea!"
        else:
            msg = "%s, do you have any fucking idea?" % target
        print(msg)

    def nfi2(self):
        if lt == 0:
            msg = "I've got no fucking idea!"
        else:
            msg = "%s, I've got no fucking idea!" % target
        print(msg)

    def nfi3(self):
        if lt == 0:
            msg = "You've got no fucking idea!"
        else:
            msg = "%s, you've clearly got no fucking idea!" % target
        print(msg)

    def nmfp1(self):
        if lt == 0:
            msg = "It's not my fucking problem."
        else:
            msg = "%s, it's not my fucking problem." % target
        print(msg)

    def nmfp2(self):
        if lt == 0:
            msg = "That's not my fucking problem."
        else:
            msg = "%s, that's not my fucking problem." % target
        print(msg)

    def nonbiz(self):
        if lt == 0:
            msg = "That's none of your fucking business."
        else:
            msg = "%s, that's none of your fucking business." % target
        print(msg)

    def noreally(self):
        if lt == 0:
            msg = "Fuck you. No really, I mean it, go fuck yourselves."
        else:
            msg = "Fuck you %s. No really, I mean it most sincerely, please go and fuck yourselves." % target
            print(msg)

    def noshit(self):
        if lt == 0:
            msg = "No shit!"
        else:
            msg = "%s, no shit!" % target
        print(msg)

    def noshitf(self):
        if lt == 0:
            msg = "No fucking shit!"
        else:
            msg = "%s, no fucking shit!" % target
        print(msg)

    def noshitfq(self):
        if lt == 0:
            msg = "No fucking shit?!"
        else:
            msg = "%s, no fucking shit?!" % target
        print(msg)

    def noshitq(self):
        if lt == 0:
            msg = "No shit?"
        else:
            msg = "%s, no shit?" % target
        print(msg)

    def noway(self):
        if lt == 0:
            msg = "No fucking way!"
        else:
            msg = "%s, there's no fucking way!" % target
        print(msg)

    def nsfch(self):
        if lt == 0:
            msg = "Not a snowflake's fucking chance in Hell!"
        else:
            msg = "%s, there's not a snowflake's fucking chance in Hell!" % target
        print(msg)

    def nsfcht(self):
        if lt == 0:
            msg = "There's not a snowflake's fucking chance in Hell of that!"
        else:
            msg = "%s, there's not a snowflake's fucking chance in Hell of that!" % target
        print(msg)

    def nsfh(self):
        if lt == 0:
            msg = "Not a snowflake's chance in Hell!"
        else:
            msg = "%s, there's not a snowflake's chance in Hell!" % target
        print(msg)

    def nsfw(self):
        if lt == 0:
            msg = "Not safe for work?  Of course it's not fucking safe for work!"
        else:
            msg = "Not safe for work?  %s, of course it's not fucking safe for work!" % target
        print(msg)

    def oath1(self):
        if lt == 0:
            msg = "Fuck oath!"
        else:
            msg = "%s, fuck oath!" % target
        print(msg)

    def oath2(self):
        if lt == 0:
            msg = "Fucking oath!"
        else:
            msg = "%s, fucking oath!" % target
        print(msg)

    def oath3(self):
        if lt == 0:
            msg = "Fuckin' oath!"
        else:
            msg = "%s, fuckin' oath!" % target
        print(msg)

    def off(self):
        if lt == 0:
            msg = "Fuck off!"
        else:
            msg = "Fuck off %s!" % target
        print(msg)

    def omnia(self):
        if lt == 0:
            msg = "Omnia quia sunt, futūtum sunt."
            # All things that are, are fucked.
        else:
            msg = "%s, omnia quia sunt, futūtum sunt." % target
        print(msg)

    def outside(self):
        if lt == 0:
            msg = "Why don't you go outside and play hide-and-go-fuck-yourself?"
        else:
            msg = "%s, why don't you go outside and play hide-and-go-fuck-yourself?" % target
        print(msg)

    def pink(self):
        msg = "Well, fuck me pink!"
        print(msg)

    def priapus(self):
        if lt == 0:
            msg = "Obscenis, peream, Priape, si non uti me pudet improbisque verbis sed cum tu posito deus pudore ostendas mihi coleos patentes cum cunno mihi mentula est vocanda."
        else:
            msg = "Obscenis, peream, %s, si non uti me pudet improbisque verbis sed cum tu posito degenerem pudore ostendas mihi coleos patentes cum cunno mihi mentula est vocanda." % target
        print(msg)

    def priapus_trans1(self):
        if lt == 0:
            msg = "I'd rather die than use obscene and improper words; but when you, as a degenerate, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks."
        else:
            msg = "I'd rather die than use obscene and improper words; but when you, %s, as a degenerate, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks." % target
        print(msg)

    def priapus_trans2(self):
        if lt == 0:
            msg = "I'd rather die than use obscene and improper words; but when you, Priapus, as a god, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks."
        else:
            msg = "I'd rather die than use obscene and improper words; but when you, %s, as an inferior, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks." % target
        print(msg)

    def psycho1(self):
        if lt == 0:
            msg = "You fucking megalomaniacal, malignantly narcissistic, psychopath!"
        else:
            msg = "%s, you fucking megalomaniacal, malignantly narcissistic, psychopath!" % target
        print(msg)

    def psycho2(self):
        if lt == 0:
            msg = "You fucking megalomaniacal, malignantly narcissistic, sociopath!"
        else:
            msg = "%s, you fucking megalomaniacal, malignantly narcissistic, sociopath!" % target
        print(msg)

    def psycho3(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, psychopath!"
        else:
            msg = "%s, you're a fucking megalomaniacal, malignantly narcissistic, psychopath!" % target
        print(msg)

    def psycho4(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, sociopath!"
        else:
            msg = "%s, you're a fucking megalomaniacal, malignantly narcissistic, sociopath!" % target
        print(msg)

    def psycho5(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, psychopathic cunt!"
        else:
            msg = "%s, you're a fucking megalomaniacal, malignantly narcissistic, psychopathic cunt!" % target
        print(msg)

    def psycho6(self):
        if lt == 0:
            msg = "You're a fucking megalomaniacal, malignantly narcissistic, sociopathic cunt!"
        else:
            msg = "%s, you're a fucking megalomaniacal, malignantly narcissistic, sociopathic cunt!" % target
        print(msg)

    def ratm(self):
        if lt == 0:
            msg = "Fuck you! I won't do what you tell me!"
        else:
            msg = "Fuck you %s! I won't do what you tell me!" % target
        print(msg)

    def roff(self):
        if lt == 0:
            msg = "You can fuck right off!"
        else:
            msg = "%s, you can fuck right off!" % target
        print(msg)

    def royal(self):
        if lt == 0:
            msg = "It's right royally fucked!"
        else:
            msg = "%s, it's right royally fucked!" % target
        print(msg)

    def royalwe(self):
        if lt == 0:
            msg = "We're right royally fucked!"
        else:
            msg = "%s, we're right royally fucked!" % target
        print(msg)

    def rtfm(self):
        if lt == 0:
            msg = "Read the fucking manual!"
        else:
            msg = "%s, read the fucking manual!" % target
        print(msg)

    def sb1(self):
        if lt == 0:
            msg = "You fucking son of a bitch!"
        else:
            msg = "%s, you fucking son of a bitch!" % target
        print(msg)

    def sb2(self):
        if lt == 0:
            msg = "You're a fucking son of a bitch!"
        else:
            msg = "%s, you're a fucking son of a bitch!" % target
        print(msg)

    def script(self):
        if lt == 0:
            msg = "Is this a script?  Of course it's a fucking script?!"
        else:
            msg = "Is this a script?  Yes %s, of course it's a fucking script?!" % target
        print(msg)

    def sfa(self):
        if lt == 0:
            msg = "Sweet fuck all."
        else:
            msg = "%s, sweet fuck all." % target
        print(msg)

    def sfac(self):
        if lt == 0:
            msg = "The chances of that are about three fifths of sweet fuck all."
        else:
            msg = "%s, the chances of that are about three fifths of sweet fuck all." % target
        print(msg)

    def shakespeare(self):
        if lt == 0:
            msg = "Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch!"
        else:
            msg = "%s, thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch!" % target
        print(msg)

    def sherlock(self):
        if lt == 0:
            msg = "No shit, Sherlock!"
        else:
            msg = "%s, no shit, Sherlock!" % target
        print(msg)

    def shit(self):
        if lt == 0:
            msg = "Fuck this shit!"
        else:
            msg = "%s, fuck your shit!" % target
        print(msg)

    def sideways(self):
        msg = "Well, fuck me sideways!"
        print(msg)

    def snafu(self):
        if lt == 0:
            msg = "Situation Normal: All Fucked Up!"
        else:
            msg = "%s, it's situation normal: all fucked up!" % target
        print(msg)

    def stfu(self):
        if lt == 0:
            msg = "Shut the fuck up!"
        else:
            msg = "%s, shut the fuck up!" % target
        print(msg)

    def stigmata(self):
        if lt == 0:
            msg = "Fuck the Church!  Fuck the State!  Fuck you!  Fuck me!  Fuck all these arseholes!"
        else:
            msg = "Fuck %s!  Fuck the Church!  Fuck the State!  Fuck you!  Fuck me!  Fuck all these arseholes!" % target
        print(msg)

    def stolen(self):
        if lt == 0:
            msg = "I wouldn't fuck you with a stolen dick!"
        else:
            msg = "I wouldn't fuck %s with a stolen dick!" % target
        print(msg)

    def survey(self):
        if lt == 0:
            msg = "Hmm, survey says ... go fuck yourself!"
        else:
            msg = "%s, survey says ... go fuck yourself!" % target
        print(msg)

    def tard(self):
        if lt == 0:
            msg = "You complete and utter fucktard!"
        else:
            msg = "%s, you are a complete and utter fucktard!" % target
        print(msg)

    def tfwo(self):
        if lt == 0:
            msg = "I'm totally fucking weirded out by that."
        else:
            msg = "%s, you're totally fucking weirding me out." % target
        print(msg)

    def thanks(self):
        if lt == 0:
            msg = "Fuck you very much."
        else:
            msg = "Fuck you very much, %s." % target
        print(msg)

    def totgaf(self):
        if lt == 0:
            msg = "I'm too old to give a fuck."
        else:
            msg = "%s, I'm too old to give a fuck." % target
        print(msg)

    def ucunt(self):
        if lt == 0:
            msg = "You cunt!"
        else:
            msg = "%s, you cunt!" % target
        print(msg)

    def up1(self):
        if lt == 0:
            msg = "I'm gonna fuck you up!"
        else:
            msg = "%s, I'm gonna fuck you up!" % target
        print(msg)

    def up2(self):
        if lt == 0:
            msg = "I'm all fucked up!"
        else:
            msg = "%s, I'm all fucked up!" % target
        print(msg)

    def up3(self):
        if lt == 0:
            msg = "I'm completely fucked up!"
        else:
            msg = "%s, I'm completely fucked up!" % target
        print(msg)

    def urcunt(self):
        if lt == 0:
            msg = "You're a cunt!"
        else:
            msg = "%s, you're a cunt!" % target
        print(msg)

    def urso1(self):
        if lt == 0:
            msg = "You are so fucked."
        else:
            msg = "You are so fucked, %s." % target
        print(msg)

    def urso2(self):
        if lt == 0:
            msg = "You are so fucked, so fucking fucked!"
        else:
            msg = "You are so fucked, %s, so fucking fucked!" % target
        print(msg)

    def utard(self):
        if lt == 0:
            msg = "You fucktard!"
        else:
            msg = "%s, you fucktard!" % target
        print(msg)

    def valley(self):
        if lt == 0:
            msg = "Yea, though I walk through the shadow of the Valley of Death I shall fear no evil ... for I am the meanest motherfucker in all the land!"
        else:
            msg = "Yea, %s, though I walk through the shadow of the Valley of Death I shall fear no evil ... for I am the meanest motherfucker in all the land!" % target
        print(msg)

    def vvv(self):
        msg = "Vidi, vici, veni."  # "I saw, I conquered, I came"
        print(msg)

    def wafwot(self):
        if lt == 0:
            msg = "What a fucking waste of time!"
        else:
            msg = "%, that's a fucking waste of time!"
        print(msg)

    def when1(self):
        if lt == 0:
            msg = "When the fuck will that happen?"
        else:
            msg = "%s, when the fuck will that happen?" % target
        print(msg)

    def when2(self):
        if lt == 0:
            msg = "When the fuck will we get there?"
        else:
            msg = "%s, when the fuck will we get there?" % target
        print(msg)

    def where1(self):
        if lt == 0:
            msg = "Where the fuck are we?"
        else:
            msg = "%s, where the fuck are we?" % target
        print(msg)

    def where2(self):
        if lt == 0:
            msg = "Where the fuck is it?"
        else:
            msg = "%s, where the fuck is it?" % target
        print(msg)

    def who1(self):
        if lt == 0:
            msg = "Who the fuck do they think you are?"
        else:
            msg = "%s, who the fuck do they think you are?" % target
        print(msg)

    def who2(self):
        if lt == 0:
            msg = "Who the fuck do you think you are?"
        else:
            msg = "%s, who the fuck do you think you are?" % target
        print(msg)

    def who3(self):
        if lt == 0:
            msg = "Who the fuck knows?"
        else:
            msg = "%s, who the fuck knows?" % target
        print(msg)

    def why(self):
        if lt == 0:
            msg = "Why the fuck should I?"
        else:
            msg = "%s, why the fuck should I?" % target
        print(msg)

    def wit(self):
        if lt == 0:
            msg = "You fuckwit!"
        else:
            msg = "%s, you fuckwit!" % target
        print(msg)

    def woftam(self):
        if lt == 0:
            msg = "It's a waste of fucking time and money."
        else:
            msg = "%s, it's a waste of fucking time and money." % target
        print(msg)

    def wtf(self):
        if lt == 0:
            msg = "What the fuck?!"
        else:
            msg = "%s, what the fuck?!" % target
        print(msg)

    def wtfc(self):
        if lt == 0:
            msg = "What fucking crack are you smoking?!"
        else:
            msg = "%s, what fucking crack are you smoking?!" % target
        print(msg)

    def wtfd(self):
        if lt == 0:
            msg = "What the fuck are you doing?!"
        else:
            msg = "%s, what the fuck are you doing?!" % target
        print(msg)

    def wtfg(self):
        if lt == 0:
            msg = "What the fuck is going on?!"
        else:
            msg = "%s, what the fuck is going on?!" % target
        print(msg)

    def wtfgh(self):
        if lt == 0:
            msg = "What the fuck is going on here?!"
        else:
            msg = "%s, what the fuck is going on here?!" % target
        print(msg)

    def wtfo(self):
        if lt == 0:
            msg = "What the fuck are you on?!"
        else:
            msg = "%s, what the fuck are you on?!" % target
        print(msg)

    def wtft(self):
        if lt == 0:
            msg = "What the fuck is that?"
        else:
            msg = "%s, what the fuck is that?" % target
        print(msg)

    def wtfta(self):
        if lt == 0:
            msg = "What the fuck are you talking about?!"
        else:
            msg = "%s, what the fuck are you talking about?!" % target
        print(msg)

    def wtfu(self):
        if lt == 0:
            msg = "What the unutterable fuck?!"
        else:
            msg = "%s, what the unutterable fuck?!" % target
        print(msg)

    def wtfwjd(self):
        if lt == 0:
            msg = "What the fuck would Jesus do?"
        else:
            msg = "%s, so what the fuck would Jesus do?" % target
        print(msg)

    def wtfwjdrtfm(self):
        if lt == 0:
            msg = "What the fuck would Jesus do?  Jesus would read the fucking manual!"
        else:
            msg = "%s, so what the fuck would Jesus do?  Jesus would read the fucking manual!" % target
        print(msg)

    def you(self):
        if lt == 0:
            msg = "Fuck you!"
        else:
            msg = "Fuck you %s!" % target
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
    print("Number of defined options:  %d" % (lc))
    print("")
elif l == 2 and wtf == "list_options":
    print("")
    print("%s  %s" % (__title__, __version__))
    print(__copyright__)
    print("")
    print("Number of defined options:  %d" % (lc))
    print("")
    print(textwrap.fill("List of defined options:  " + ", ".join(df), 72))
    print("")
    print("Bitcoin:  %s" % __bitcoin__)
    print("")
elif l >= 3 and wtf == "sherlock" and target.lower()[0:8] == "sherlock":
    print("No shit, Sherlock!")
elif l >= 3 and wtf == "random" and rc == "sherlock" and target.lower()[0:8] == "sherlock":
    print("No shit, Sherlock!")
elif l == 2 and wtf == "unittest":
    print(about)
    print("")
    for i in range(lc):
        print("Command:  %s -f %s [-n %s]" % (sa[0], df[i]))
        try:
            exec("fuck()."+df[i]+"()")
        except(AttributeError, NameError):
            print("Fuck testing!")
        print("")
elif l >= 3 and wtf == "unittest":
    if target.lower() == "atitle":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "copyright":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "website":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "adversary":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "domain":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "donations":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "bitcoin":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "author":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "contact":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "email":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "encryption":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "gpg key":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "options":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "pirate":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "twitter":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "twython tools":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "version":
        print("Command:  %s -f about -n %s" % (sa[0], target.lower))
        exec("fuck().about()")
        print("")
    elif target.lower() == "carnal":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "bond":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "die":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "right":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "title":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "cunt":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "foaas":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "snag":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "snafu":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "fubar":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "lmfao":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    elif target.lower() == "figjam":
        print("Command:  %s -f acronym -n %s" % (sa[0], target.lower))
        exec("fuck().acronym()")
        print("")
    else:
        print(about)
        print("")
        for i in range(lc):
            print("Command:  %s -f %s [-n %s]" % (sa[0], df[i], target))
            try:
                exec("fuck()."+df[i]+"()")
            except(AttributeError, NameError):
                print("Fuck testing!")
            print("")
elif l >= 2 and wtf == "random":
    try:
        exec("fuck()."+rc+"()")
    except(AttributeError, NameError):
        print("Fuck randomness!")
elif la == 3:
    if args.fuck is not None and args.name is None:
        try:
            exec("fuck()."+wtf+"()")
        except(AttributeError, NameError):
            print("Fuck %s!" % wtf)
    elif args.fuck is None and args.name is not None:
        print("Fuck %s!" % target)
elif la == 4:
    if args.fuck is not None and args.name is None:
        try:
            exec("fuck()."+wtf+"()")
        except(AttributeError, NameError):
            w = []
            for i in range(la - 2):
                w.append(str(sys.argv[i + 2]))
            wtf = " ".join(w)
            print("Fuck %s!" % wtf)
    elif args.fuck is None and args.name is not None:
        t = []
        for i in range(la - 2):
            t.append(str(sys.argv[i + 2]))
        target = " ".join(t)
        print("Fuck %s!" % target)
    elif args.fuck is not None and args.name is not None:
        try:
            exec("fuck()."+wtf+"()")
        except(AttributeError, NameError):
            print("Fuck %s!" % wtf)
    else:
        pass
        # print("Fuck Perl!")
elif la >= 5:
    if args.fuck is not None and args.name is None:
        try:
            exec("fuck()."+wtf+"()")
        except(AttributeError, NameError):
            w = []
            for i in range(la - 2):
                w.append(str(sys.argv[i + 2]))
            wtf = " ".join(w)
            print("Fuck %s!" % wtf)
    elif args.fuck is None and args.name is not None:
        t = []
        for i in range(la - 2):
            t.append(str(sys.argv[i + 2]))
        target = " ".join(t)
        print("Fuck %s!" % target)
    elif args.fuck is not None and args.name is not None:
        try:
            exec("fuck()."+wtf+"()")
        except(AttributeError, NameError):
            w = []
            for i in range(la - 2):
                if str(sys.argv[i]).startswith("-") is False:
                    w.append(str(sys.argv[i + 2]))
            wtfx = " ".join(w)
            print("Fuck %s!" % wtfx)
