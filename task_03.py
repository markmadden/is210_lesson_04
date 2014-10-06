#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" task 4 """

import data

MAXIMUM = None
MINIMUM = None
DAYS = 0
TOTAL = 0

for DAY in data.TRANSACTIONS:
    DAYS += 1
    DAY_TOTAL = 0
    for TRANS in DAY:
        DAY_TOTAL += TRANS

    if DAY_TOTAL < MINIMUM or MINIMUM is None:
        print MINIMUM, DAY_TOTAL 
        MINIMUM = DAY_TOTAL      
        
    if DAY_TOTAL > MAXIMUM or MAXIMUM is None:
        print MAXIMUM, DAY_TOTAL
        MAXIMUM = DAY_TOTAL
        

    TOTAL += DAY_TOTAL
