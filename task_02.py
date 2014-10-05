#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 2 Week 4 Homework """

import data
ACCESS = False
COUNTER = 4
while not ACCESS:
    COUNTER -= 1
    MESSAGE = 'Enter the password please.: ({0} attempts remain)'.format(COUNTER)
    PASS = raw_input(MESSAGE)
    if COUNTER <2:
        print "Access denied. Try again later"
        break;
    if data.PASSWORD == PASS:
        ACCESS = True
        print "Access Is Granted."
