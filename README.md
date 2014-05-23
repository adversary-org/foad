FOAD: Fucked Off Adversarial Degenerates
========================================

Text based script for readily insulting people intended to be run from
the command line or in IRC.  Can be incorporated into other scripts,
such as [Twython Tools](https://github.com/adversary-org/twython-tools).

To use it run: foad.py [-h/--help] -f/--fuck option [-n/--name target]

Examples:

```
bash-3.2$ ./foad.py -f wtfwjd
What the fuck would Jesus do?
bash-3.2$ ./foad.py -f wtfwjdrtfm -n Bob
Bob, so what the fuck would Jesus do?  Jesus would read the fucking manual!
bash-3.2$ ./foad.py -f mind -n "Joe Biden"
Joe Biden, are you out of your fucking mind?!
bash-3.2$ foad -f psycho3 -n "Tony Abbott"
Tony Abbott, you're a fucking megalomaniacal, malignantly narcissistic, psychopath!
bash-3.2$ 
```

There are currently more than 160 options to use with the -f flag and
the majority of those have two forms, one for naming a subject and a
more general one.  As well as a couple of special options which are
more informative than insulting.  The full list of options is visible
on the command line by running "foad.py -f list_options" and the test
script will generate most of the possible output.

If you find this script of use or even just amusing, a small Bitcoin
contribution to 1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz would be
appreciated.


## Requirements

* Python 3.2 and above.
* Only utilises standard modules (argparse, sys, random and a couple
  of others).
