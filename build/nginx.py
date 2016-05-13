#!/usr/bin/env python

import os.path


with open(os.path.join(os.path.dirname(__file__), '..', 'database.txt')) as database:
    for line in database:
        print('deny {};'.format(line.split('#')[0].strip()))
