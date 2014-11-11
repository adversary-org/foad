FOAD: Fucked Off Adversarial Degenerates
========================================

Text based script for readily insulting people intended to be run from
the command line or in IRC.  Can be incorporated into other scripts,
such as [Twython Tools](https://github.com/adversary-org/twython-tools).

To use it run: foad.py [-h/--help] -f/--fuck option [-n/--name target] [-s/--sender from] [-e/--extra "some paramater"] [-p/--prepend "text before insult"] [-a/--append "text after insult"]

Examples:

```
bash$ ./foad.py -f wtfwjd
What the fuck would Jesus do?
bash$ ./foad.py -f wtfwjdrtfm -n Bob
Bob, so what the fuck would Jesus do?  Jesus would read the fucking manual!
bash$ ./foad.py -f mind -n "Joe Biden"
Joe Biden, are you out of your fucking mind?!
bash$ foad -f psycho3 -n "Tony Abbott"
Tony Abbott, you're a fucking megalomaniacal, malignantly narcissistic, psychopath!
bash$ 
```

There are currently more than 200 options to use with the -f flag and
the majority of those have two or more forms, one for naming a
subject, a more general one and occasionally a sender or extra text
appended.  As well as a couple of special options which are more
informative than insulting.  The full list of options is visible on
the command line by running "foad.py -f list_options" and the test
script will generate most of the possible output.  All options and the
generic catchall can now be used with --prepend and/or --append.

If you find this script of use or even just amusing, a small Bitcoin
contribution to 1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz would be
appreciated.


## Requirements

* Python 3.2 and above.
* Only utilises standard modules (argparse, sys, random and a couple
  of others).
* Utilises the new standard for string formatting as of version 0.7.
