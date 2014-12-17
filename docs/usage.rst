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
