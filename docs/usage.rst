==========
Using FOAD
==========


For the most part foad.py is fairly straight forward and obvious, but
there are some areas in which problems might arise and there are some
options which do not use the existing flags in an expected manner.


Command Line
============

The most common use of foad.py will be directly on the command line or
some slight variation thereof.  Aside from behavioural changes with
certain options, the only thing to really be wary of is passing
variables which contain characters normally treated differently on the
command line being used.  For example in bash the grave accent is used
to execute commands, so a name containing that character will need to
have an escape character like a backslash preceding it.


IRC
===

Many IRC clients support some method of passing command line commands
to the interface and for the most part foad.py will behave no
differently than any other command.


XChat and HexChat
-----------------

Both XChat and HexChat include their own instance of Python generally
a release of Python 2.  In recent HexChat versions it is Python 2.7.5.
This is what enables the use of IRC plugins written in Python.

Since foad.py uses Python 3.2 or greater, there may be conflicts
between the version of Python it calls and that used by XChat or
HexChat, though this does not appear to be consistent across all
platforms.  Usually the culprit relates to the $PYTHONPATH value or
other environment settings.

If this occurs then the solution is to wrap the foad.py command in a
script which temporarily overrides the default XChat or HexChat
settings in order to run that command and return the foad.py output.
An example of this, written for HexChat 2.10.0 on OS X systems is
included in the project (the osxpy3-foad.sh file).  Users needing this
should make sure the paths in that file are correct for their systems.
Essentially, though, it just sets values/paths for $PYTHON,
$PYTHONHOME and $PYTHONPATH, then it calls foad.py and appends any
command line parameters or arguments.

Use of a script like this will not be necessary in most cases, but
where it is necessary this shell script wrapper is quite sufficient to
deal with it.  Even with HexChat it appears to no longer be necessary
when changing the version of OS X from 10.5 to 10.9 and changing the
version of HexChat from 2.10.0 to 2.10.1.  Though it is only a hunch,
I suspect the fix was in HexChat rather than OS X, but that is simply
based on the author of HexChat being more approachable than HexChat.


SMS
===

As with the Twitter code described below, it is quite possible to
utilise foad.py with any script which accesses an SMS gateway via an
API (usually a RESTful or old HTTP-Post API).


Twitter
=======


There are plenty of Twitter clients out there and even a number of
command line ones.  Once again, if they can call on the text output of
a command then they ought to be able to utilise foad.py.


Twython
-------

Twython is one of, if not the, best Pythonic solutions for dealing
with Twitter.  I already use it extensively as the section on Twython
Tools below indicates.

See the `Twython repository <https://github.com/ryanmcgrath/twython>`__ or the `Twython documentation <https://twython.readthedocs.org/en/latest/>`__ for more
details.


Twython Tools
-------------

Most of my general Twitter usage is through Twittering Mode for Emacs,
but I've also got a handful of scripts using Twython, bundled together
with the unimaginitive title of Twython Tools.  Currently each one
supports a single function, though there will be a gradual move to
less scripts with greater detail and lots of argparse flags.

Unlike foad.py, Twython Tools includes several requirements not
bundled with Python by default, but all of those requirements are
either included or easily obtainable using Pip or Easy Install.

One of those requirements is the PyCrypto module which is used to
securely store authentication data (OAuth data) when it is not in use.

The most common usage with foad.py would be with the basic tweeting
script.  Here are a couple of examples:

    tweet-basic.py \`foad.py -f fascinating -n "George Brandis"\`

This would send a tweet which said:

    Fascinating story, George Brandis, in what chapter do you shut the fuck up?

Alternatively there's something like this:

    tweet-basic.py \`foad.py -f kirsan -n @TonyAbbottMHR\`

This would send a tweet which said:

    @TonyAbbottMHR, you are as corrupt, delusional, megalomaniacal, vindictive and just as fucking crazy as that fucktard Kirsan Ilyumzhinov!

One thing to be careful of here, however, is that some output exceeds the 140 character limit on Twitter and the basic script does not include message length checks.  Note that there is an archive which includes scripts specifically designed for use with foad.py, these functions will be returned as part of the switch to using argparse.

See the `Twython Tools repository <https://github.com/adversary-org/twython-tools>`__ on GitHub for more details.
