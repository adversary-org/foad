FOAD: Fucked Off Adversarial Degenerates
========================================

Text based script for readily insulting people intended to be run from
the command line or in IRC. Can be incorporated into other scripts, such
as `Twython Tools <https://github.com/adversary-org/twython-tools>`__.

To use it run:

::

    foad.py [-h/--help] -f/--fuck option [-n/--name target] [-s/--sender from] [-e/--extra "some paramater"] [-p/--prepend "text before insult"] [-a/--append "text after insult"]

Examples:

::

    bash$ ./foad.py -f wtfwjd
    What the fuck would Jesus do?
    bash$
    
    bash$ ./foad.py -f wtfwjdrtfm -n Bob
    So Bob, what the fuck would Jesus do?  Jesus would read the fucking manual!
    bash$
    
    bash$ ./foad.py -f mind -n "Mike Pence"
    Mike Pence, are you out of your fucking mind?!
    bash$
    
    bash$ foad -f psycho3 -n "Tony Abbott"
    Tony Abbott, you're a fucking megalomaniacal, malignantly narcissistic, psychopath!
    bash$
    
    bash$ foad -f priapus1 -n @fatneckbeardguy
    Obscenis, peream, @fatneckbeardguy, si non uti me pudet improbisque verbis sed cum tu posito degenerem pudore ostendas mihi coleos patentes cum cunno mihi mentula est vocanda.
    bash$
    
    bash$ foad -f priapus1 -n @fatneckbeardguy | wrap -w 78
    Obscenis, peream, @fatneckbeardguy, si non uti me pudet improbisque verbis sed
    cum tu posito degenerem pudore ostendas mihi coleos patentes cum cunno mihi
    mentula est vocanda.
    bash$ 
    
    bash$ foad -f priapus1 -n @fatneckbeardguy -e trans
    I'd rather die than use obscene and improper words; but when you, @fatneckbeardguy, as a degenerate, appear with your testicles hanging out, it is appropriate for me to speak of cunts and cocks.
    bash$
    
    bash$ foad -f priapus1 -n @fatneckbeardguy -e trans | wrap -w 78
    I'd rather die than use obscene and improper words; but when you,
    @fatneckbeardguy, as a degenerate, appear with your testicles hanging out, it
    is appropriate for me to speak of cunts and cocks.
    bash$ 


There are currently more than 200 options to use with the ``-f`` flag
and the majority of those have two or more forms, one for naming a
subject, a more general one and occasionally a sender or extra text or
other parameter included. As well as a couple of special options which
are more informative than insulting. The full list of options is
visible on the command line by running ``foad.py -O .`` and the test
script will generate most of the possible output. All options and the
generic catchall can now be used with ``--prepend`` and/or
``--append``.

Note that though the Latin example abobe and its corresponding
translated text via the ``--extra`` flag utilise a Twitter-style
username, that output is actually too long for a tweet.  It would work
as a DM, though.

If you find this script of use or even just amusing, a small Bitcoin
contribution to ``1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz`` would be
appreciated.


Installing
----------

All you need to do to install this script is download foad.py and move
it to somewhere in your path. See the Requirements section for the
version of Python required. To import it as a module in Python it needs
to be in your Python path (e.g. site-packages). I usually just leave it
in /usr/local/bin or $HOME/bin with an appropriately adjusted .bashrc or
.bash\_profile configuration.

The script should be obtained from here:

https://github.com/adversary-org/foad


Requirements
------------

-  Python 3.2 and above by default (see below).
-  Only utilises standard modules (argparse, sys, random and a couple of
   others).
-  Utilises the new standard for string formatting as of version 0.7.

Optional Python 2.7 Support
---------------------------

- From Version 0.8 support for Python 2.7 has been restored.
- Will not work with Python 2.6 or earlier.
- Requires changing the first line to call python2 or python
  (depending on the platform) instead of python3.
- Operation ought to match the existing methods.
- If there is ever some kind of conflict between Python 2 and Python
  3, any changes made will favour Python 3.  If it is necessary to
  disable this (by removing the ``from __future__`` import) then that
  will be done.
