#!/bin/bash

export PYTHON="/Library/Frameworks/Python.framework/Versions/3.4/bin/python3" && export PYTHONHOME="/Library/Frameworks/Python.framework/Versions/3.4" && export PYTHONPATH="/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4:/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages" && exec /usr/local/bin/foad.py "$@"
